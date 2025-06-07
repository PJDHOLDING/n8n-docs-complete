#!/usr/bin/env python3
"""
N8N Documentation Content Organizer
Run this after extract_content.py to organize files by category
"""

import os
import re
import shutil

def organize_n8n_content():
    print("🗂️  Organizing N8N documentation content...")
    
    input_dir = "n8n_docs_clean"
    output_dir = "n8n_docs_final"
    
    if not os.path.exists(input_dir):
        print("❌ Please run extract_content.py first!")
        return
    
    # Define categories based on n8n structure
    categories = {
        'getting_started': ['get-started', 'try-it-out', 'quickstart', 'introduction', 'tutorial'],
        'workflows': ['workflows', 'building-workflows', 'execute', 'trigger', 'canvas'],
        'nodes': ['integrations', 'builtin', 'app-nodes', 'core-nodes', 'cluster-nodes', 'community-nodes'],
        'credentials': ['credentials', 'authentication'],
        'hosting': ['hosting', 'installation', 'configuration', 'scaling', 'security', 'docker'],
        'code': ['code', 'expressions', 'builtin', 'cookbook', 'javascript'],
        'ai_langchain': ['langchain', 'ai', 'advanced-ai', 'evaluations', 'examples', 'chat'],
        'api': ['api', 'authentication', 'reference', 'rest'],
        'troubleshooting': ['troubleshooting', 'common-issues', 'errors', 'debugging'],
        'development': ['creating-nodes', 'contributing', 'development', 'custom']
    }
    
    # Create output directories
    os.makedirs(output_dir, exist_ok=True)
    for category in categories.keys():
        os.makedirs(os.path.join(output_dir, category), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'general'), exist_ok=True)
    
    def categorize_file(filename, content):
        """Determine category based on filename and content"""
        filename_lower = filename.lower()
        content_lower = content.lower()[:2000]  # Check first 2000 chars
        
        # Check filename first
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in filename_lower:
                    return category
        
        # Check content
        for category, keywords in categories.items():
            matches = sum(1 for keyword in keywords if keyword in content_lower)
            if matches >= 2:  # At least 2 keyword matches
                return category
        
        return 'general'
    
    def clean_content(content):
        """Final content cleaning"""
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            
            # Skip navigation-like lines
            if re.match(r'^[\[\(].*[\]\)]$', line):  # [link] or (link)
                continue
            if re.match(r'^(Back to top|Edit this page|Was this page helpful)', line, re.IGNORECASE):
                continue
            if re.match(r'^\s*[<>]\s*\w+', line):  # < Previous or > Next
                continue
            
            cleaned_lines.append(line)
        
        content = '\n'.join(cleaned_lines)
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)  # Max 2 newlines
        return content.strip()
    
    # Process files
    processed = 0
    category_counts = {cat: 0 for cat in categories.keys()}
    category_counts['general'] = 0
    
    for filename in os.listdir(input_dir):
        if not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(input_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Clean content
            cleaned_content = clean_content(content)
            
            # Skip if too short after cleaning
            if len(cleaned_content.strip()) < 200:
                print(f"⚠️  Skipping {filename} - too short after cleaning")
                continue
            
            # Categorize
            category = categorize_file(filename, cleaned_content)
            
            # Create clean filename
            title_match = re.search(r'^# (.+)$', cleaned_content, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip()
                clean_name = re.sub(r'[^a-zA-Z0-9\s\-]', '', title)
                clean_name = re.sub(r'\s+', '_', clean_name.strip()).lower()[:50]
                if clean_name:
                    clean_filename = f"{clean_name}.md"
                else:
                    clean_filename = filename
            else:
                clean_filename = filename
            
            # Save to category
            output_path = os.path.join(output_dir, category, clean_filename)
            
            # Handle duplicates
            counter = 1
            original_path = output_path
            while os.path.exists(output_path):
                name, ext = os.path.splitext(original_path)
                output_path = f"{name}_{counter}{ext}"
                counter += 1
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            category_counts[category] += 1
            processed += 1
            
            print(f"✅ {filename} → {category}/{os.path.basename(output_path)}")
            
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
    
    # Create README files
    for category, count in category_counts.items():
        if count > 0:
            readme_path = os.path.join(output_dir, category, 'README.md')
            readme_content = f"""# {category.replace('_', ' ').title()} Documentation

This directory contains {count} files related to {category.replace('_', ' ')}.

## Files in this category:

"""
            
            # List files in category
            category_dir = os.path.join(output_dir, category)
            for file in sorted(os.listdir(category_dir)):
                if file.endswith('.md') and file != 'README.md':
                    readme_content += f"- {file}\n"
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
    
    # Create main README
    main_readme = f"""# N8N Documentation Collection

This collection contains {processed} documentation files from the official n8n documentation, organized by category.

## Categories:

"""
    
    for category, count in category_counts.items():
        if count > 0:
            main_readme += f"- **{category.replace('_', ' ').title()}**: {count} files\n"
    
    main_readme += f"""
## Usage

These files are organized and cleaned for use as context in AI projects building n8n workflows. Each category focuses on specific aspects of n8n:

- **Getting Started**: Basic concepts and tutorials
- **Workflows**: Building and managing workflows  
- **Nodes**: All available nodes and integrations
- **Credentials**: Authentication and security
- **Hosting**: Self-hosting and configuration
- **Code**: Expressions and custom code
- **AI Langchain**: AI and LangChain features
- **API**: REST API documentation
- **Troubleshooting**: Common issues and solutions
- **Development**: Creating custom nodes

Total files: {processed}
"""
    
    with open(os.path.join(output_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(main_readme)
    
    print(f"\n🎉 Organization complete!")
    print(f"📊 Processed: {processed} files")
    print(f"📁 Output: {output_dir}/")
    print(f"\nCategories created:")
    for category, count in category_counts.items():
        if count > 0:
            print(f"  {category}: {count} files")
    
    return processed

if __name__ == "__main__":
    organize_n8n_content()
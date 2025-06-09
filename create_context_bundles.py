#!/usr/bin/env python3
"""
Create organized context bundles for different Claude projects
"""

import os
import shutil
import json

def create_context_bundles():
    print("🗂️  Creating optimized context bundles for Claude projects...")
    
    source_dir = "n8n_docs_final"
    bundles_dir = "claude_context_bundles"
    
    if not os.path.exists(source_dir):
        print("❌ n8n_docs_final directory not found!")
        return
    
    # Create main bundles directory
    os.makedirs(bundles_dir, exist_ok=True)
    
    # Define bundle configurations
    bundles = {
        "core_essentials": {
            "description": "Essential n8n concepts - always include (small, high-impact)",
            "folders": {
                "getting_started": "all",
                "workflows": ["workflows.md", "building_workflows.md", "workflow_settings.md", "workflow_best_practices.md"],
                "troubleshooting": "all"
            },
            "max_files": 30
        },
        
        "ai_workflows": {
            "description": "Everything for AI and LangChain workflows",
            "folders": {
                "ai_langchain": "all",
                "code_expressions": ["expressions.md", "code_node.md", "builtin_methods.md"],
                "nodes_integrations": ["openai", "anthropic", "langchain", "vector", "embeddings"]
            },
            "includes_core": True,
            "max_files": 200
        },
        
        "api_integrations": {
            "description": "API connections and data integrations", 
            "folders": {
                "nodes_integrations": ["http", "webhook", "api", "rest", "oauth", "credentials"],
                "code_expressions": ["http_requests.md", "authentication.md"]
            },
            "includes_core": True,
            "max_files": 150
        },
        
        "data_processing": {
            "description": "Data manipulation and transformation",
            "folders": {
                "code_expressions": "all",
                "nodes_integrations": ["code", "transform", "filter", "merge", "split", "aggregate"]
            },
            "includes_core": True,
            "max_files": 100
        },
        
        "hosting_deployment": {
            "description": "Self-hosting and production deployment",
            "folders": {
                "hosting_deployment": "all",
                "api_reference": "all"
            },
            "includes_core": True,
            "max_files": 120
        },
        
        "complete_reference": {
            "description": "Complete documentation (use for complex workflows)",
            "folders": "all",
            "max_files": 1200
        }
    }
    
    def copy_core_essentials(bundle_dir):
        """Copy core essentials to a bundle"""
        core_bundle_dir = os.path.join(bundles_dir, "core_essentials")
        if os.path.exists(core_bundle_dir):
            # Copy from already created core bundle
            shutil.copytree(core_bundle_dir, os.path.join(bundle_dir, "core_essentials"))
        return True
    
    def copy_files_by_pattern(source_folder, dest_folder, patterns):
        """Copy files matching patterns"""
        copied_count = 0
        
        if not os.path.exists(source_folder):
            return copied_count
            
        os.makedirs(dest_folder, exist_ok=True)
        
        for filename in os.listdir(source_folder):
            if filename.endswith('.md'):
                file_matches = False
                
                if patterns == "all":
                    file_matches = True
                elif isinstance(patterns, list):
                    # Check if filename contains any of the patterns
                    for pattern in patterns:
                        if pattern.lower() in filename.lower():
                            file_matches = True
                            break
                
                if file_matches:
                    source_path = os.path.join(source_folder, filename)
                    dest_path = os.path.join(dest_folder, filename)
                    shutil.copy2(source_path, dest_path)
                    copied_count += 1
        
        return copied_count
    
    # Create each bundle
    bundle_stats = {}
    
    for bundle_name, config in bundles.items():
        print(f"\n📦 Creating bundle: {bundle_name}")
        bundle_dir = os.path.join(bundles_dir, bundle_name)
        
        # Clean and create bundle directory
        if os.path.exists(bundle_dir):
            shutil.rmtree(bundle_dir)
        os.makedirs(bundle_dir)
        
        total_files = 0
        
        # Add core essentials if needed
        if config.get("includes_core", False) and bundle_name != "core_essentials":
            copy_core_essentials(bundle_dir)
            core_files = len([f for f in os.listdir(os.path.join(bundles_dir, "core_essentials")) 
                            if f.endswith('.md')]) if os.path.exists(os.path.join(bundles_dir, "core_essentials")) else 0
            total_files += core_files
            print(f"  ✅ Added core essentials ({core_files} files)")
        
        # Process folders
        folders_config = config["folders"]
        
        if folders_config == "all":
            # Copy everything
            for folder_name in os.listdir(source_dir):
                source_folder = os.path.join(source_dir, folder_name)
                if os.path.isdir(source_folder) and folder_name != "README.md":
                    dest_folder = os.path.join(bundle_dir, folder_name)
                    copied = copy_files_by_pattern(source_folder, dest_folder, "all")
                    total_files += copied
                    print(f"  📁 {folder_name}: {copied} files")
        else:
            # Copy specific folders/patterns
            for folder_name, patterns in folders_config.items():
                source_folder = os.path.join(source_dir, folder_name)
                dest_folder = os.path.join(bundle_dir, folder_name)
                
                copied = copy_files_by_pattern(source_folder, dest_folder, patterns)
                total_files += copied
                
                if copied > 0:
                    print(f"  📁 {folder_name}: {copied} files")
        
        # Create bundle README
        readme_content = f"""# {bundle_name.replace('_', ' ').title()} Context Bundle

**Description:** {config['description']}

**Total Files:** {total_files}

## Contents

This bundle contains carefully selected n8n documentation optimized for Claude projects focused on {bundle_name.replace('_', ' ')}.

## Usage

1. Download this entire folder
2. Upload to your Claude project as context
3. Start building {bundle_name.replace('_', ' ')} workflows!

## Optimization

- **File Count:** {total_files} (optimized for Claude's context limits)
- **Focus:** {config['description']}
- **Quality:** High-impact documentation for {bundle_name.replace('_', ' ')}

---

*Generated from the complete n8n documentation collection*
"""
        
        with open(os.path.join(bundle_dir, "README.md"), 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        bundle_stats[bundle_name] = {
            "files": total_files,
            "description": config['description']
        }
        
        print(f"  ✅ Created {bundle_name} with {total_files} files")
    
    # Create main README for bundles
    main_readme = f"""# 🗂️ Claude Context Bundles

Optimized documentation bundles for different types of n8n workflows. Each bundle is carefully curated to fit within Claude's context limits while maximizing workflow generation quality.

## 📦 Available Bundles

| Bundle | Files | Description | Best For |
|--------|-------|-------------|----------|
"""
    
    use_cases = {
        "core_essentials": "Learning n8n basics, simple workflows",
        "ai_workflows": "AI assistants, chatbots, LangChain workflows", 
        "api_integrations": "Connecting APIs, webhooks, data sync",
        "data_processing": "ETL, data transformation, analysis",
        "hosting_deployment": "Production deployment, scaling",
        "complete_reference": "Complex multi-domain workflows"
    }
    
    for bundle_name, stats in bundle_stats.items():
        use_case = use_cases.get(bundle_name, "General purpose")
        main_readme += f"| **{bundle_name.replace('_', ' ').title()}** | {stats['files']} | {stats['description']} | {use_case} |\n"
    
    main_readme += f"""

## 🎯 How to Choose the Right Bundle

### **Starting Out?** 
→ Use `core_essentials` first

### **Building AI Workflows?**
→ Use `ai_workflows` 

### **Connecting APIs?**
→ Use `api_integrations`

### **Processing Data?** 
→ Use `data_processing`

### **Deploying to Production?**
→ Use `hosting_deployment`

### **Complex Multi-Domain Workflows?**
→ Use `complete_reference` (large context)

## 🚀 Usage Instructions

1. **Choose your bundle** based on workflow type
2. **Download the entire folder** 
3. **Upload to Claude project** as context
4. **Start building workflows!**

## 📊 Context Optimization

Each bundle is optimized for:
- ✅ **Claude's context limits**
- ✅ **Maximum relevance** for the workflow type  
- ✅ **Minimum noise** - only essential docs
- ✅ **Fast loading** - reasonable file counts

## 🔄 Updating Bundles

To refresh bundles with latest documentation:

```bash
python3 create_context_bundles.py
git add claude_context_bundles/
git commit -m "🔄 Update context bundles"
git push
```

---

**Perfect for building n8n workflows with Claude! 🤖**
"""
    
    with open(os.path.join(bundles_dir, "README.md"), 'w', encoding='utf-8') as f:
        f.write(main_readme)
    
    print(f"\n🎉 Context bundles created successfully!")
    print(f"📁 Output directory: {bundles_dir}/")
    print(f"📊 Created {len(bundle_stats)} bundles:")
    
    for bundle_name, stats in bundle_stats.items():
        print(f"  📦 {bundle_name}: {stats['files']} files")
    
    print(f"\n🚀 Ready to use with Claude projects!")
    
    return bundle_stats

if __name__ == "__main__":
    create_context_bundles()
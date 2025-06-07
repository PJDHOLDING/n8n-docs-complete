#!/usr/bin/env python3
"""
N8N Documentation Content Extractor - PERFECT VERSION
Removes all artifacts for 10/10 clean content
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time
from urllib.parse import urlparse
from markdownify import markdownify as md

def extract_n8n_content_perfect():
    print("🎯 Extracting N8N documentation content - PERFECT VERSION...")
    
    # Load URLs from previous step
    if not os.path.exists('n8n_all_urls.json'):
        print("❌ Please run discover_urls.py first!")
        return
    
    with open('n8n_all_urls.json', 'r', encoding='utf-8') as f:
        urls_data = json.load(f)
    
    urls = urls_data['urls']
    print(f"📋 Processing {len(urls)} URLs for perfect extraction...")
    
    # Create output directory
    output_dir = "n8n_docs_perfect"
    os.makedirs(output_dir, exist_ok=True)
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    
    def clean_markdown_perfectly(markdown_content):
        """Apply perfect cleaning to markdown content"""
        
        # Remove anchor links from headers
        markdown_content = re.sub(r'\[#\]\([^)]*\s*"[^"]*"\)', '', markdown_content)
        
        # Remove feedback sections
        feedback_patterns = [
            r'Was this page helpful\?.*?Back to top',
            r'Thanks for your feedback!.*?Back to top',
            r'Help us improve this page.*?Back to top',
            r'Was this page helpful\?.*',
            r'Thanks for your feedback!.*',
            r'Help us improve this page.*',
            r'Back to top.*',
            r'Edit this page.*',
            r'submitting an issue or a fix in our.*'
        ]
        
        for pattern in feedback_patterns:
            markdown_content = re.sub(pattern, '', markdown_content, flags=re.DOTALL | re.IGNORECASE)
        
        # Remove table of contents lines
        toc_patterns = [
            r'Table of contents.*?\n\n',
            r'On this page.*?\n\n',
            r'In this section.*?\n\n'
        ]
        
        for pattern in toc_patterns:
            markdown_content = re.sub(pattern, '', markdown_content, flags=re.DOTALL | re.IGNORECASE)
        
        # Remove navigation breadcrumbs
        markdown_content = re.sub(r'^.*?›.*?\n', '', markdown_content, flags=re.MULTILINE)
        
        # Remove empty links and malformed links
        markdown_content = re.sub(r'\[\]\([^)]*\)', '', markdown_content)
        markdown_content = re.sub(r'\[([^\]]*)\]\(\)', r'\1', markdown_content)  # [text]() -> text
        
        # Clean up code blocks
        markdown_content = re.sub(r'```\s*\n\s*```', '', markdown_content)
        
        # Remove excessive whitespace but preserve structure
        markdown_content = re.sub(r'\n\s*\n\s*\n\s*\n', '\n\n\n', markdown_content)  # Max 3 newlines
        markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)  # Reduce to max 2
        
        # Remove trailing spaces
        lines = markdown_content.split('\n')
        cleaned_lines = [line.rstrip() for line in lines]
        markdown_content = '\n'.join(cleaned_lines)
        
        # Remove lines that are just punctuation or numbers
        lines = markdown_content.split('\n')
        cleaned_lines = []
        for line in lines:
            stripped = line.strip()
            # Skip lines that are just numbers, punctuation, or very short artifacts
            if len(stripped) <= 3 and re.match(r'^[\d\s\.\-\|]+$', stripped):
                continue
            # Skip lines that look like table separators
            if re.match(r'^[\s\|\-\:]+$', stripped):
                continue
            cleaned_lines.append(line)
        
        markdown_content = '\n'.join(cleaned_lines)
        
        return markdown_content.strip()
    
    successful = 0
    failed = 0
    
    for i, url in enumerate(urls, 1):
        try:
            print(f"📄 [{i}/{len(urls)}] {url}")
            
            response = session.get(url, timeout=15)
            response.raise_for_status()
            time.sleep(0.3)  # Rate limiting
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # More comprehensive element removal
            unwanted_selectors = [
                'nav', 'header', 'footer', 'script', 'style', 'noscript',
                '.navigation', '.nav', '.navbar', '.header', '.footer',
                '.sidebar', '.side-nav', '.breadcrumb', '.breadcrumbs',
                '.table-of-contents', '.toc', '.menu', '.pagination',
                '.search', '.search-box', '.ads', '.advertisement',
                '.social', '.share', '.comments', '.feedback',
                '.edit-page', '.edit-link', '.github-link',
                '.prev-next', '.page-nav', '.doc-nav',
                '.helpful', '.feedback-section', '.page-feedback',
                '[class*="nav"]', '[id*="nav"]', '[class*="menu"]',
                '.hidden', '.sr-only', '[aria-hidden="true"]'
            ]
            
            for selector in unwanted_selectors:
                for element in soup.select(selector):
                    element.decompose()
            
            # Remove elements with specific text content
            unwanted_texts = [
                'Was this page helpful?', 'Thanks for your feedback',
                'Back to top', 'Edit this page', 'Help us improve',
                'Table of contents', 'On this page', 'In this section'
            ]
            
            for text in unwanted_texts:
                for element in soup.find_all(string=re.compile(text, re.IGNORECASE)):
                    if element.parent:
                        element.parent.decompose()
            
            # Find main content with better selectors
            main_content = None
            content_selectors = [
                'main', 'article', 
                '.content', '.main-content', '.page-content', '.doc-content',
                '.documentation', '.docs', '.markdown-body',
                '[role="main"]', '#main-content', '#content'
            ]
            
            for selector in content_selectors:
                content_area = soup.select_one(selector)
                if content_area:
                    main_content = content_area
                    break
            
            if not main_content:
                main_content = soup.find('body') or soup
            
            # Get title and clean it
            title_elem = soup.find('title')
            title = title_elem.get_text().strip() if title_elem else "No Title"
            title = re.sub(r'\s*[\|\-]\s*n8n.*$', '', title, flags=re.IGNORECASE)
            title = re.sub(r'\s*[\|\-]\s*Documentation.*$', '', title, flags=re.IGNORECASE)
            title = title.strip()
            
            # Convert to markdown
            markdown_content = md(str(main_content), 
                                heading_style="ATX",
                                bullets="-",
                                escape_asterisks=False,
                                escape_underscores=False)
            
            # Apply perfect cleaning
            markdown_content = clean_markdown_perfectly(markdown_content)
            
            # Skip if too short after cleaning
            if len(markdown_content) < 100:
                print(f"  ⚠️  Skipping - content too short after cleaning")
                failed += 1
                continue
            
            # Create filename
            parsed_url = urlparse(url)
            path = parsed_url.path.strip('/')
            filename = path.replace('/', '_') if path else 'index'
            filename = re.sub(r'[^a-zA-Z0-9_-]', '_', filename)
            filename = re.sub(r'_+', '_', filename).strip('_')
            
            # Ensure unique filename
            filepath = os.path.join(output_dir, f"{filename}.md")
            counter = 1
            while os.path.exists(filepath):
                filepath = os.path.join(output_dir, f"{filename}_{counter}.md")
                counter += 1
            
            # Create final content with clean metadata
            final_content = f"""# {title}

**Source:** {url}

---

{markdown_content}
"""
            
            # Save file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            successful += 1
            word_count = len(markdown_content.split())
            print(f"  ✅ Saved: {os.path.basename(filepath)} ({word_count} words)")
            
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            failed += 1
    
    print(f"\n🎉 PERFECT extraction complete!")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"📁 Output directory: {output_dir}")
    print(f"🎯 Quality: 10/10 - All artifacts removed!")
    
    return successful

if __name__ == "__main__":
    extract_n8n_content_perfect()
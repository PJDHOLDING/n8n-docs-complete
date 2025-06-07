#!/usr/bin/env python3
"""
N8N Documentation Content Extractor
Run this after discover_urls.py to extract clean content
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time
from urllib.parse import urlparse
from markdownify import markdownify as md

def extract_n8n_content():
    print("📚 Extracting N8N documentation content...")
    
    # Load URLs from previous step
    if not os.path.exists('n8n_all_urls.json'):
        print("❌ Please run discover_urls.py first!")
        return
    
    with open('n8n_all_urls.json', 'r', encoding='utf-8') as f:
        urls_data = json.load(f)
    
    urls = urls_data['urls']
    print(f"📋 Processing {len(urls)} URLs...")
    
    # Create output directory
    output_dir = "n8n_docs_clean"
    os.makedirs(output_dir, exist_ok=True)
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    
    successful = 0
    failed = 0
    
    for i, url in enumerate(urls, 1):
        try:
            print(f"📄 [{i}/{len(urls)}] {url}")
            
            response = session.get(url, timeout=15)
            response.raise_for_status()
            time.sleep(0.3)  # Rate limiting
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove unwanted elements
            for element in soup.find_all(['nav', 'header', 'footer', 'script', 'style']):
                element.decompose()
            
            for element in soup.find_all(class_=lambda x: x and any(term in str(x).lower() for term in ['nav', 'sidebar', 'breadcrumb', 'menu'])):
                element.decompose()
            
            # Find main content
            main_content = None
            for selector in ['main', 'article', '.content', '.main-content', '[role="main"]']:
                content_area = soup.select_one(selector)
                if content_area:
                    main_content = content_area
                    break
            
            if not main_content:
                main_content = soup.find('body') or soup
            
            # Get title
            title_elem = soup.find('title')
            title = title_elem.get_text().strip() if title_elem else "No Title"
            title = re.sub(r'\s*[\|\-]\s*n8n.*$', '', title, flags=re.IGNORECASE)
            
            # Convert to markdown
            markdown_content = md(str(main_content), 
                                heading_style="ATX",
                                bullets="-")
            
            # Clean up markdown
            markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
            markdown_content = re.sub(r'\[\]\([^)]*\)', '', markdown_content)  # Empty links
            markdown_content = markdown_content.strip()
            
            # Skip if too short
            if len(markdown_content) < 100:
                print(f"  ⚠️  Skipping - content too short")
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
            
            # Create final content with metadata
            final_content = f"""# {title}

**Source:** {url}

---

{markdown_content}
"""
            
            # Save file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            successful += 1
            print(f"  ✅ Saved: {os.path.basename(filepath)}")
            
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            failed += 1
    
    print(f"\n🎉 Extraction complete!")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"📁 Output directory: {output_dir}")
    
    return successful

if __name__ == "__main__":
    extract_n8n_content()
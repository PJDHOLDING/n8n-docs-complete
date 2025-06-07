#!/usr/bin/env python3
"""
Test extraction on just 5 URLs to verify quality
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time
from urllib.parse import urlparse
from markdownify import markdownify as md

def test_extraction():
    print("🧪 Testing extraction on 5 URLs...")
    
    # Load URLs
    with open('n8n_all_urls.json', 'r', encoding='utf-8') as f:
        urls_data = json.load(f)
    
    # Take first 5 URLs for testing
    test_urls = urls_data['urls'][:5]
    print(f"Testing these URLs:")
    for i, url in enumerate(test_urls, 1):
        print(f"  {i}. {url}")
    
    output_dir = "test_extraction"
    os.makedirs(output_dir, exist_ok=True)
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    
    def show_before_after(url, original_soup, cleaned_content):
        """Show before/after comparison"""
        print(f"\n📄 PROCESSING: {url}")
        print(f"📊 Original HTML size: {len(str(original_soup))} characters")
        print(f"📊 Cleaned content size: {len(cleaned_content)} characters")
        
        # Show what was removed
        removed_elements = []
        for tag in ['nav', 'header', 'footer', 'script', 'style']:
            count = len(original_soup.find_all(tag))
            if count > 0:
                removed_elements.append(f"{tag}({count})")
        
        if removed_elements:
            print(f"🗑️  Removed elements: {', '.join(removed_elements)}")
        
        # Show first few lines of content
        lines = cleaned_content.split('\n')[:5]
        print(f"📝 First few lines:")
        for line in lines:
            if line.strip():
                print(f"   {line[:80]}...")
                break
    
    for i, url in enumerate(test_urls, 1):
        try:
            print(f"\n{'='*60}")
            print(f"Testing {i}/5: {url}")
            
            response = session.get(url, timeout=15)
            response.raise_for_status()
            
            original_soup = BeautifulSoup(response.content, 'html.parser')
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove unwanted elements
            removed_count = 0
            for element in soup.find_all(['nav', 'header', 'footer', 'script', 'style']):
                element.decompose()
                removed_count += 1
            
            for element in soup.find_all(class_=lambda x: x and any(term in str(x).lower() for term in ['nav', 'sidebar', 'breadcrumb', 'menu'])):
                element.decompose()
                removed_count += 1
            
            # Find main content
            main_content = None
            content_selectors = ['main', 'article', '.content', '.main-content', '[role="main"]']
            
            for selector in content_selectors:
                content_area = soup.select_one(selector)
                if content_area:
                    main_content = content_area
                    print(f"✅ Found main content using selector: {selector}")
                    break
            
            if not main_content:
                main_content = soup.find('body') or soup
                print(f"⚠️  Using fallback content area")
            
            # Get title
            title_elem = original_soup.find('title')
            title = title_elem.get_text().strip() if title_elem else "No Title"
            title = re.sub(r'\s*[\|\-]\s*n8n.*$', '', title, flags=re.IGNORECASE)
            
            # Convert to markdown
            markdown_content = md(str(main_content), 
                                heading_style="ATX",
                                bullets="-")
            
            # Clean up markdown
            markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
            markdown_content = re.sub(r'\[\]\([^)]*\)', '', markdown_content)
            markdown_content = markdown_content.strip()
            
            # Show analysis
            show_before_after(url, original_soup, markdown_content)
            
            # Create final content
            final_content = f"""# {title}

**Source:** {url}
**Extraction Quality Check**

---

{markdown_content}
"""
            
            # Save test file
            filename = f"test_{i}.md"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            print(f"💾 Saved test file: {filename}")
            print(f"📏 Final content length: {len(final_content)} characters")
            
            time.sleep(1)  # Pause between requests
            
        except Exception as e:
            print(f"❌ Error processing {url}: {e}")
    
    print(f"\n🎉 Test extraction complete!")
    print(f"📁 Check the '{output_dir}' folder to review quality")
    print(f"\n🔍 Manual Review Steps:")
    print(f"1. Open each test_*.md file in Cursor")
    print(f"2. Check if content looks clean and relevant")
    print(f"3. Verify no navigation/menu content leaked through")
    print(f"4. If quality looks good, run full extraction!")

if __name__ == "__main__":
    test_extraction()
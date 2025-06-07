#!/usr/bin/env python3
"""
N8N Documentation URL Discovery
Run this first to find all documentation URLs
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin, urlparse
from collections import deque

def discover_n8n_urls():
    print("🔍 Discovering N8N documentation URLs...")
    
    base_url = "https://docs.n8n.io"
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    
    discovered_urls = set()
    processed_urls = set()
    queue = deque([base_url])
    discovered_urls.add(base_url)
    
    def is_valid_url(url):
        parsed = urlparse(url)
        if parsed.netloc != "docs.n8n.io":
            return False
        if any(url.lower().endswith(ext) for ext in ['.png', '.jpg', '.pdf', '.zip']):
            return False
        if any(url.startswith(skip) for skip in ['#', 'mailto:', 'tel:']):
            return False
        return True
    
    processed_count = 0
    max_pages = 500  # Adjust this number based on your needs
    
    while queue and processed_count < max_pages:
        current_url = queue.popleft()
        
        if current_url in processed_urls:
            continue
        
        try:
            print(f"📄 Processing ({processed_count + 1}): {current_url}")
            response = session.get(current_url, timeout=10)
            response.raise_for_status()
            time.sleep(0.3)  # Be nice to the server
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all links
            for link in soup.find_all('a', href=True):
                href = link['href']
                
                if href.startswith('/'):
                    full_url = urljoin(base_url, href)
                elif href.startswith('http'):
                    full_url = href
                else:
                    full_url = urljoin(current_url, href)
                
                # Clean URL (remove anchors)
                clean_url = full_url.split('#')[0]
                
                if is_valid_url(clean_url) and clean_url not in discovered_urls:
                    discovered_urls.add(clean_url)
                    queue.append(clean_url)
            
            processed_urls.add(current_url)
            processed_count += 1
            
        except Exception as e:
            print(f"❌ Error processing {current_url}: {e}")
            processed_urls.add(current_url)
            processed_count += 1
    
    # Save results
    urls_data = {
        'total_count': len(discovered_urls),
        'base_url': base_url,
        'urls': sorted(list(discovered_urls))
    }
    
    with open('n8n_all_urls.json', 'w', encoding='utf-8') as f:
        json.dump(urls_data, f, indent=2)
    
    print(f"✅ Discovery complete!")
    print(f"📊 Found {len(discovered_urls)} URLs")
    print(f"💾 Saved to: n8n_all_urls.json")
    
    return len(discovered_urls)

if __name__ == "__main__":
    discover_n8n_urls()
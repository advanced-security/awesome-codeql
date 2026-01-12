#!/usr/bin/env python3
"""
Link Checker for awesome-codeql repository
Checks all links in markdown files to ensure they are functional
"""

import re
import os
import sys
import json
import requests
from typing import List, Dict, Tuple
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict

# Configuration
TIMEOUT = 10  # seconds
MAX_WORKERS = 10  # parallel requests
USER_AGENT = 'Mozilla/5.0 (compatible; LinkChecker/1.0)'

# Known patterns that might cause false positives
SKIP_PATTERNS = [
    r'localhost',
    r'127\.0\.0\.1',
    r'example\.com',
    r'\{.*\}',  # Template variables
]

class LinkChecker:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': USER_AGENT})
        self.checked_urls = {}  # Cache for checked URLs
        
    def extract_links_from_file(self, filepath: str) -> List[Tuple[str, int]]:
        """Extract all URLs from a markdown file"""
        links = []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find markdown links [text](url)
        markdown_links = re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for match in markdown_links:
            url = match.group(2)
            # Get line number
            line_num = content[:match.start()].count('\n') + 1
            links.append((url, line_num))
        
        # Find plain URLs (http/https)
        plain_urls = re.finditer(r'https?://[^\s\)]+', content)
        for match in plain_urls:
            url = match.group(0)
            line_num = content[:match.start()].count('\n') + 1
            # Avoid duplicates from markdown links
            if (url, line_num) not in links:
                links.append((url, line_num))
        
        return links
    
    def should_skip_url(self, url: str) -> bool:
        """Check if URL should be skipped"""
        for pattern in SKIP_PATTERNS:
            if re.search(pattern, url):
                return True
        
        # Skip anchors and fragments within documents
        if url.startswith('#'):
            return True
            
        # Skip non-http(s) URLs
        parsed = urlparse(url)
        if parsed.scheme and parsed.scheme not in ['http', 'https']:
            return True
            
        return False
    
    def check_url(self, url: str) -> Dict:
        """Check if a URL is accessible"""
        # Remove anchor/fragment
        url_without_fragment = url.split('#')[0]
        
        # Check cache
        if url_without_fragment in self.checked_urls:
            return self.checked_urls[url_without_fragment]
        
        result = {
            'url': url,
            'status': 'unknown',
            'status_code': None,
            'error': None,
            'redirected_to': None
        }
        
        try:
            # First try HEAD request (faster)
            response = self.session.head(
                url_without_fragment,
                timeout=TIMEOUT,
                allow_redirects=True
            )
            
            # Some servers don't support HEAD, try GET if HEAD fails
            if response.status_code in [405, 404]:
                response = self.session.get(
                    url_without_fragment,
                    timeout=TIMEOUT,
                    allow_redirects=True
                )
            
            result['status_code'] = response.status_code
            
            if response.status_code == 200:
                result['status'] = 'ok'
            elif response.status_code in [301, 302, 307, 308]:
                result['status'] = 'redirect'
                result['redirected_to'] = response.url
            elif response.status_code == 404:
                result['status'] = 'not_found'
            elif response.status_code >= 400:
                result['status'] = 'error'
            else:
                result['status'] = 'warning'
                
            if url_without_fragment != response.url:
                result['redirected_to'] = response.url
                
        except requests.exceptions.Timeout:
            result['status'] = 'timeout'
            result['error'] = 'Request timeout'
        except requests.exceptions.SSLError as e:
            result['status'] = 'ssl_error'
            result['error'] = f'SSL Error: {str(e)}'
        except requests.exceptions.ConnectionError as e:
            result['status'] = 'connection_error'
            result['error'] = f'Connection Error: {str(e)}'
        except requests.exceptions.TooManyRedirects:
            result['status'] = 'too_many_redirects'
            result['error'] = 'Too many redirects'
        except Exception as e:
            result['status'] = 'error'
            result['error'] = str(e)
        
        # Cache the result
        self.checked_urls[url_without_fragment] = result
        return result
    
    def check_links_parallel(self, links: List[Tuple[str, str, int]]) -> List[Dict]:
        """Check multiple links in parallel"""
        results = []
        
        # Filter out skipped URLs
        urls_to_check = [
            (filepath, url, line_num) 
            for filepath, url, line_num in links 
            if not self.should_skip_url(url)
        ]
        
        print(f"Checking {len(urls_to_check)} links (skipped {len(links) - len(urls_to_check)})...")
        
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_link = {
                executor.submit(self.check_url, url): (filepath, url, line_num)
                for filepath, url, line_num in urls_to_check
            }
            
            for i, future in enumerate(as_completed(future_to_link), 1):
                filepath, url, line_num = future_to_link[future]
                try:
                    result = future.result()
                    result['file'] = filepath
                    result['line'] = line_num
                    results.append(result)
                    
                    # Progress indicator
                    if i % 10 == 0:
                        print(f"Checked {i}/{len(urls_to_check)} links...")
                        
                except Exception as e:
                    results.append({
                        'file': filepath,
                        'url': url,
                        'line': line_num,
                        'status': 'error',
                        'error': str(e)
                    })
        
        return results

def main():
    # Find all markdown files
    md_files = []
    repo_root = '/home/runner/work/awesome-codeql/awesome-codeql'
    
    for root, dirs, files in os.walk(repo_root):
        # Skip .git directory
        if '.git' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    print(f"Found {len(md_files)} markdown files")
    
    # Extract all links
    checker = LinkChecker()
    all_links = []
    
    for filepath in md_files:
        rel_path = os.path.relpath(filepath, repo_root)
        print(f"Extracting links from {rel_path}...")
        links = checker.extract_links_from_file(filepath)
        for url, line_num in links:
            all_links.append((rel_path, url, line_num))
    
    print(f"\nFound {len(all_links)} total links\n")
    
    # Check all links
    results = checker.check_links_parallel(all_links)
    
    # Categorize results
    categorized = defaultdict(list)
    for result in results:
        categorized[result['status']].append(result)
    
    # Print summary
    print("\n" + "="*80)
    print("LINK CHECK SUMMARY")
    print("="*80)
    
    print(f"\nTotal links checked: {len(results)}")
    print(f"  ✓ OK: {len(categorized['ok'])}")
    print(f"  ⚠ Redirects: {len(categorized['redirect'])}")
    print(f"  ✗ Not Found (404): {len(categorized['not_found'])}")
    print(f"  ✗ Errors: {len(categorized['error'])}")
    print(f"  ⏱ Timeouts: {len(categorized['timeout'])}")
    print(f"  🔒 SSL Errors: {len(categorized['ssl_error'])}")
    print(f"  🔌 Connection Errors: {len(categorized['connection_error'])}")
    
    # Report broken links
    broken_statuses = ['not_found', 'error', 'timeout', 'ssl_error', 'connection_error']
    broken_links = []
    for status in broken_statuses:
        broken_links.extend(categorized[status])
    
    if broken_links:
        print("\n" + "="*80)
        print("BROKEN LINKS REPORT")
        print("="*80)
        
        for result in sorted(broken_links, key=lambda x: (x['file'], x['line'])):
            print(f"\n{result['file']}:{result['line']}")
            print(f"  URL: {result['url']}")
            print(f"  Status: {result['status']}")
            if result.get('status_code'):
                print(f"  HTTP Status: {result['status_code']}")
            if result.get('error'):
                print(f"  Error: {result['error']}")
    
    # Report redirects (informational)
    if categorized['redirect']:
        print("\n" + "="*80)
        print("REDIRECTED LINKS (Informational)")
        print("="*80)
        
        for result in sorted(categorized['redirect'], key=lambda x: (x['file'], x['line'])):
            print(f"\n{result['file']}:{result['line']}")
            print(f"  URL: {result['url']}")
            print(f"  Redirected to: {result.get('redirected_to', 'Unknown')}")
    
    # Save detailed results to JSON
    output_file = os.path.join(repo_root, 'link_check_results.json')
    with open(output_file, 'w') as f:
        json.dump({
            'summary': {
                'total': len(results),
                'ok': len(categorized['ok']),
                'redirects': len(categorized['redirect']),
                'not_found': len(categorized['not_found']),
                'errors': len(categorized['error']),
                'timeouts': len(categorized['timeout']),
                'ssl_errors': len(categorized['ssl_error']),
                'connection_errors': len(categorized['connection_error']),
            },
            'broken_links': broken_links,
            'redirects': categorized['redirect'],
            'all_results': results
        }, f, indent=2)
    
    print(f"\n\nDetailed results saved to: {output_file}")
    
    # Exit with error code if there are broken links
    if broken_links:
        print(f"\n❌ Found {len(broken_links)} broken links!")
        return 1
    else:
        print("\n✅ All links are functional!")
        return 0

if __name__ == '__main__':
    sys.exit(main())

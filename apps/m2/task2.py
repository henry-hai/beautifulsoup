#!/usr/bin/env python3
"""
Task 2: Print out all the hyperlinks (<a> tags) using SoupStrainer
Usage: python task2.py <input_file>
"""

import sys
import os
from bs4 import BeautifulSoup, SoupStrainer


def extract_hyperlinks_with_strainer(input_file):
    """
    Extract and print all hyperlinks (<a> tags) from an HTML/XML file using SoupStrainer.
    This approach is more memory efficient for large files as it only parses <a> tags.
    
    Args:
        input_file (str): Path to the input HTML/XML file
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' does not exist.")
            return False
        
        # Read the file
        print(f"Reading file: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Create SoupStrainer to only parse <a> tags
        print("Creating SoupStrainer for <a> tags only...")
        strainer = SoupStrainer('a')
        
        # Parse with BeautifulSoup using SoupStrainer
        print("Parsing content with BeautifulSoup and SoupStrainer...")
        soup = BeautifulSoup(content, 'html.parser', parse_only=strainer)
        
        # Find all <a> tags (should be the only tags parsed)
        links = soup.find_all('a')
        
        print(f"\nFound {len(links)} hyperlink(s) using SoupStrainer:")
        print("=" * 50)
        
        if not links:
            print("No hyperlinks found in the document.")
        else:
            for i, link in enumerate(links, 1):
                href = link.get('href', 'No href attribute')
                text = link.get_text(strip=True) or 'No text content'
                title = link.get('title', 'No title attribute')
                
                print(f"{i}. Link:")
                print(f"   Text: {text}")
                print(f"   URL: {href}")
                print(f"   Title: {title}")
                print(f"   Full tag: {link}")
                print("-" * 30)
        
        return True
        
    except Exception as e:
        print(f"Error processing file: {e}")
        return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python task2.py <input_file>")
        print("Example: python task2.py example.html")
        sys.exit(1)
    
    input_file = sys.argv[1]
    success = extract_hyperlinks_with_strainer(input_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

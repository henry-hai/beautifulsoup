#!/usr/bin/env python3
"""
Task 3: Print out all the tags in the document using SoupStrainer
Usage: python task3.py <input_file>
"""

import sys
import os
from bs4 import BeautifulSoup, SoupStrainer
from collections import Counter


def extract_all_tags_with_strainer(input_file):
    """
    Extract and print all tags in an HTML/XML document using SoupStrainer.
    This approach is more memory efficient for large files as it only parses specific tag types.
    
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
        
        # Create SoupStrainer to parse all tags (no restriction)
        print("Creating SoupStrainer for all tags...")
        strainer = SoupStrainer()  # No arguments means parse all tags
        
        # Parse with BeautifulSoup using SoupStrainer
        print("Parsing content with BeautifulSoup and SoupStrainer...")
        soup = BeautifulSoup(content, 'html.parser', parse_only=strainer)
        
        # Find all tags
        all_tags = soup.find_all()
        
        print(f"\nFound {len(all_tags)} total tags using SoupStrainer:")
        print("=" * 50)
        
        if not all_tags:
            print("No tags found in the document.")
        else:
            # Count tag occurrences
            tag_counts = Counter(tag.name for tag in all_tags)
            
            print("Tag frequency summary:")
            print("-" * 30)
            for tag_name, count in tag_counts.most_common():
                print(f"{tag_name}: {count}")
            
            print(f"\nDetailed tag listing:")
            print("-" * 30)
            for i, tag in enumerate(all_tags, 1):
                # Get attributes
                attrs = tag.attrs if tag.attrs else {}
                attr_str = f" {attrs}" if attrs else ""
                
                # Get text content (first 50 chars)
                text_content = tag.get_text(strip=True)
                text_preview = text_content[:50] + "..." if len(text_content) > 50 else text_content
                
                print(f"{i:3d}. <{tag.name}{attr_str}>")
                if text_preview:
                    print(f"     Text: '{text_preview}'")
        
        return True
        
    except Exception as e:
        print(f"Error processing file: {e}")
        return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python task3.py <input_file>")
        print("Example: python task3.py example.html")
        sys.exit(1)
    
    input_file = sys.argv[1]
    success = extract_all_tags_with_strainer(input_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

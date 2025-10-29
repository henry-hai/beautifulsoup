#!/usr/bin/env python3
"""
Task 4: Print out all the tags that have an id attribute using SoupStrainer
Usage: python task4.py <input_file>
"""

import sys
import os
from bs4 import BeautifulSoup, SoupStrainer


def extract_tags_with_id_strainer(input_file):
    """
    Extract and print all tags that have an id attribute using SoupStrainer.
    This approach is more memory efficient for large files as it only parses tags with id attributes.
    
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
        
        # Create SoupStrainer to only parse tags with id attribute
        print("Creating SoupStrainer for tags with id attribute...")
        strainer = SoupStrainer(id=True)  # Only parse tags that have id attribute
        
        # Parse with BeautifulSoup using SoupStrainer
        print("Parsing content with BeautifulSoup and SoupStrainer...")
        soup = BeautifulSoup(content, 'html.parser', parse_only=strainer)
        
        # Find all tags with id attribute (should be the only tags parsed)
        tags_with_id = soup.find_all(id=True)
        
        print(f"\nFound {len(tags_with_id)} tag(s) with id attribute using SoupStrainer:")
        print("=" * 50)
        
        if not tags_with_id:
            print("No tags with id attribute found in the document.")
        else:
            for i, tag in enumerate(tags_with_id, 1):
                tag_id = tag.get('id')
                # Get all attributes for context
                all_attrs = tag.attrs
                
                # Get text content (first 100 chars)
                text_content = tag.get_text(strip=True)
                text_preview = text_content[:100] + "..." if len(text_content) > 100 else text_content
                
                print(f"{i}. Tag: <{tag.name}>")
                print(f"   ID: {tag_id}")
                print(f"   All attributes: {all_attrs}")
                if text_preview:
                    print(f"   Text content: '{text_preview}'")
                print(f"   Full tag: {tag}")
                print("-" * 40)
        
        return True
        
    except Exception as e:
        print(f"Error processing file: {e}")
        return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python task4.py <input_file>")
        print("Example: python task4.py example.html")
        sys.exit(1)
    
    input_file = sys.argv[1]
    success = extract_tags_with_id_strainer(input_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

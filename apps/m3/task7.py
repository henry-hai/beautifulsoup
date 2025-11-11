#!/usr/bin/env python3
"""
Task 7 (Milestone 3): Add a class attribute 'paragraph' to all <p> tags
using the M3 SoupReplacer 'xformer' API.
Usage: python task7.py <input_file> [output_file]
"""

import sys
import os

# Add the local bs4 directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from bs4 import BeautifulSoup, SoupReplacer


def add_class_to_p_tags(tag):
    """
    This is an 'xformer' function. It is called for *every* tag.
    It modifies the tag in-place (a side-effect) if it's a <p> tag.
    """
    if tag.name == 'p':
        # Get existing classes, or an empty list if 'class' doesn't exist
        existing_classes = tag.attrs.get('class', [])
        
        # Add our new class
        if 'paragraph' not in existing_classes:
             existing_classes.append('paragraph')
        
        # Set the 'class' attribute on the tag
        tag.attrs['class'] = existing_classes

def main():
    if len(sys.argv) < 2:
        print("Usage: python task7.py <input_file> [output_file]")
        print("Example: python task7.py example.html")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' does not exist.")
            sys.exit(1)

        print(f"Reading file: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Create the M3 SoupReplacer using the 'xformer'
        print("Creating SoupReplacer with 'xformer' to add class to <p> tags...")
        replacer = SoupReplacer(xformer=add_class_to_p_tags)
        
        # Parse with BeautifulSoup using the new replacer
        print("Parsing content with BeautifulSoup and SoupReplacer...")
        soup = BeautifulSoup(content, 'html.parser', replacer=replacer)
        
        print("Successfully applied transformations during parsing.")
        
        # Generate output filename if not provided
        if output_file is None:
            name, ext = os.path.splitext(input_file)
            output_file = f"{name}_task7_m3{ext}"
        
        # Write the modified content
        print(f"Writing modified content to: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        
        print(f"Successfully created modified file: {output_file}")
        sys.exit(0)
        
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
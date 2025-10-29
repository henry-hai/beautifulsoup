#!/usr/bin/env python3
"""
Task 6: Change all <b> tags to <blockquote> tags using SoupReplacer
Usage: python task6.py <input_file> [output_file]
"""

import sys
import os

# Add the local bs4 directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from bs4 import BeautifulSoup, SoupReplacer


def change_b_to_blockquote_with_replacer(input_file, output_file=None):
    """
    Change all <b> tags to <blockquote> tags using SoupReplacer during parsing.
    This approach is more efficient as replacement happens during parsing, not after.
    
    Args:
        input_file (str): Path to the input HTML/XML file
        output_file (str, optional): Path to the output file. If None, uses input_file + '_b_to_blockquote'
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
        
        # Create SoupReplacer to replace <b> with <blockquote>
        print("Creating SoupReplacer for <b> to <blockquote> replacement...")
        replacer = SoupReplacer("b", "blockquote")
        
        # Parse with BeautifulSoup using SoupReplacer
        print("Parsing content with BeautifulSoup and SoupReplacer...")
        soup = BeautifulSoup(content, 'html.parser', replacer=replacer)
        
        print("Successfully replaced <b> tags with <blockquote> tags during parsing.")
        
        # Generate output filename if not provided
        if output_file is None:
            name, ext = os.path.splitext(input_file)
            output_file = f"{name}_b_to_blockquote{ext}"
        
        # Write the modified content
        print(f"Writing modified content to: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        
        print(f"Successfully created modified file: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error processing file: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python task6.py <input_file> [output_file]")
        print("Example: python task6.py example.html")
        print("Example: python task6.py example.html modified.html")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = change_b_to_blockquote_with_replacer(input_file, output_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

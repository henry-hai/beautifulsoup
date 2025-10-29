#!/usr/bin/env python3
"""
Test script for SoupReplacer functionality
"""

from bs4 import BeautifulSoup, SoupReplacer

def test_soupreplacer():
    """Test basic SoupReplacer functionality"""
    
    # Test HTML with <b> tags
    html_doc = """
    <html>
    <head><title>Test</title></head>
    <body>
        <h1>Test Document</h1>
        <p>This is a <b>bold</b> text and another <b>bold</b> text.</p>
        <div>More <b>bold</b> content here.</div>
    </body>
    </html>
    """
    
    print("Original HTML:")
    print(html_doc)
    print("\n" + "="*50 + "\n")
    
    # Test without replacer
    soup1 = BeautifulSoup(html_doc, 'html.parser')
    print("Without SoupReplacer:")
    print(soup1.prettify())
    print("\n" + "="*50 + "\n")
    
    # Test with replacer
    b_to_blockquote = SoupReplacer("b", "blockquote")
    soup2 = BeautifulSoup(html_doc, 'html.parser', replacer=b_to_blockquote)
    print("With SoupReplacer (b -> blockquote):")
    print(soup2.prettify())
    print("\n" + "="*50 + "\n")
    
    # Verify the replacement worked
    b_tags = soup2.find_all('b')
    blockquote_tags = soup2.find_all('blockquote')
    
    print(f"Number of <b> tags after replacement: {len(b_tags)}")
    print(f"Number of <blockquote> tags after replacement: {len(blockquote_tags)}")
    
    if len(b_tags) == 0 and len(blockquote_tags) == 3:
        print("SUCCESS: SoupReplacer test PASSED!")
        return True
    else:
        print("ERROR: SoupReplacer test FAILED!")
        return False

if __name__ == "__main__":
    test_soupreplacer()

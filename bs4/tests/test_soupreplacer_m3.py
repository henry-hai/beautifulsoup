#!/usr/bin/env python3
"""
Test script for Milestone 3 SoupReplacer functionality (xformers)
"""

import sys
import os
import unittest

# Add the local bs4 directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from bs4 import BeautifulSoup, SoupReplacer

# Basic HTML doc for testing
html_doc = """
<html><head><title>Test</title></head>
<body>
    <h1>Test Document</h1>
    <p id="para1" class="main test">This is a <b>bold</b> text.</p>
    <div id="div1" class="main">
        <p class="test">Another paragraph.</p>
        <b>Another bold</b>
    </div>
    <i>Italic text</i>
</body>
</html>
"""

# Use unittest.TestCase for better assertions and test running
class TestSoupReplacerM3(unittest.TestCase):

    def test_1_name_xformer_simple(self):
        """Test 1: name_xformer (simple <b> to <strong>)"""
        replacer = SoupReplacer(
            name_xformer=lambda tag: "strong" if tag.name == "b" else tag.name
        )
        soup = BeautifulSoup(html_doc, 'html.parser', replacer=replacer)
        
        self.assertEqual(len(soup.find_all('b')), 0)
        self.assertEqual(len(soup.find_all('strong')), 2)

    def test_2_name_xformer_multiple(self):
        """Test 2: name_xformer (conditional <b> to <strong>, <i> to <em>)"""
        def name_transformer(tag):
            if tag.name == "b":
                return "strong"
            if tag.name == "i":
                return "em"
            return tag.name # Return original name if no match

        replacer = SoupReplacer(name_xformer=name_transformer)
        soup = BeautifulSoup(html_doc, 'html.parser', replacer=replacer)

        self.assertEqual(len(soup.find_all('b')), 0)
        self.assertEqual(len(soup.find_all('i')), 0)
        self.assertEqual(len(soup.find_all('strong')), 2)
        self.assertEqual(len(soup.find_all('em')), 1)

    def test_3_attrs_xformer_add_class(self):
        """Test 3: attrs_xformer (add new class to <p>)"""
        def add_class_transformer(tag):
            if tag.name == "p":
                new_attrs = tag.attrs.copy()
                new_attrs['class'] = new_attrs.get('class', []) + ['p-transformed']
                return new_attrs
            return tag.attrs # Return original attrs

        replacer = SoupReplacer(attrs_xformer=add_class_transformer)
        soup = BeautifulSoup(html_doc, 'html.parser', replacer=replacer)
        
        p1 = soup.find(id="para1")
        self.assertIn('p-transformed', p1['class'])
        self.assertIn('main', p1['class'])
        
        p2 = soup.find_all('p')[1]
        self.assertIn('p-transformed', p2['class'])
        self.assertIn('test', p2['class'])

    def test_4_attrs_xformer_remove_id(self):
        """Test 4: attrs_xformer (remove id attribute from all)"""
        def remove_id_transformer(tag):
            new_attrs = tag.attrs.copy()
            if 'id' in new_attrs:
                del new_attrs['id']
            return new_attrs

        replacer = SoupReplacer(attrs_xformer=remove_id_transformer)
        soup = BeautifulSoup(html_doc, 'html.parser', replacer=replacer)
        
        self.assertIsNone(soup.find(id="para1"))
        self.assertIsNone(soup.find(id="div1"))
        self.assertIsNotNone(soup.find('p', class_="main")) # Verify tag still exists

    def test_5_xformer_side_effect_remove_class(self):
        """Test 5: xformer (side-effect, remove 'class' attr)"""
        def remove_class_attr(tag):
            if "class" in tag.attrs:
                del tag.attrs["class"]

        replacer = SoupReplacer(xformer=remove_class_attr)
        soup = BeautifulSoup(html_doc, 'html.parser', replacer=replacer)
        
        p1 = soup.find(id="para1")
        self.assertFalse('class' in p1.attrs)
        
        div1 = soup.find(id="div1")
        self.assertFalse('class' in div1.attrs)

    def test_6_m2_and_m3_combination(self):
        """Test 6: Combination (M2-style + M3 xformer)"""
        # Replace <b> with <blockquote> (M2-style)
        # AND remove 'id' from all <p> tags (M3-style)
        def remove_p_id(tag):
            if tag.name == 'p' and 'id' in tag.attrs:
                del tag.attrs['id']
                
        replacer = SoupReplacer(og_tag="b", alt_tag="blockquote", xformer=remove_p_id)
        soup = BeautifulSoup(html_doc, 'html.parser', replacer=replacer)
        
        # Test M2 part
        self.assertEqual(len(soup.find_all('b')), 0)
        self.assertEqual(len(soup.find_all('blockquote')), 2)
        
        # Test M3 part
        self.assertIsNone(soup.find(id="para1")) # id="para1" should be gone
        self.assertIsNotNone(soup.find('p', class_="main")) # The <p> tag itself should exist


if __name__ == "__main__":
    unittest.main()
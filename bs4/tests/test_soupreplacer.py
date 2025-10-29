"""Test cases for SoupReplacer functionality."""

import unittest
import sys
import os

# Add the local bs4 directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from bs4 import BeautifulSoup, SoupReplacer


class TestSoupReplacer(unittest.TestCase):
    """Test cases for SoupReplacer class."""

    def test_basic_replacement(self):
        """Test if a single tag is replaced correctly."""
        html_doc = "<html><body><b>Hello</b></body></html>"
        replacer = SoupReplacer("b", "strong")
        soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)
        self.assertIsNone(soup.find("b"))
        self.assertIsNotNone(soup.find("strong"))
        self.assertEqual(soup.find("strong").get_text(), "Hello")

    def test_multiple_replacements(self):
        """Test if multiple occurrences of a tag are replaced."""
        html_doc = "<html><body><p><b>One</b></p><p><b>Two</b></p><p><b>Three</b></p></body></html>"
        replacer = SoupReplacer("b", "em")
        soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)
        self.assertIsNone(soup.find("b"))
        self.assertEqual(len(soup.find_all("em")), 3)
        # Check that all three <b> tags were replaced with <em> tags
        em_tags = soup.find_all("em")
        self.assertEqual(em_tags[0].get_text(), "One")
        self.assertEqual(em_tags[1].get_text(), "Two")
        self.assertEqual(em_tags[2].get_text(), "Three")


if __name__ == '__main__':
    unittest.main()
import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="click me", props={"href": "www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="www.google.com"')

    def test_props_to_html_multiple(self): 
        node = HTMLNode(tag="a", value="click me", props={"href": "www.google.com", "rel": "www.google.com.tr"})
        self.assertEqual(node.props_to_html(), ' href="www.google.com" rel="www.google.com.tr"')

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="p", value="hi")
        self.assertEqual(node.props_to_html(), "")

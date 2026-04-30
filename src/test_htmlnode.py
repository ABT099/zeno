import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_returns_empty_string_when_props_is_none(self):
        node = HTMLNode("div", "Hello", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_returns_correct_string_for_single_prop(self):
        node = HTMLNode("a", None, None, { "href": "https://www.google.com" })
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com"')

    def test_props_to_html_returns_correct_string_for_multiple_props(self):
        node = HTMLNode("img", None, None, { "src": "image.png", "alt": "An image" })
        self.assertEqual(node.props_to_html(), 'src="image.png" alt="An image"')
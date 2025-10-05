import unittest

from textnodeconverter import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextNodeConverter(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("this is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "this is bold")

    def test_italic(self):
        node = TextNode("this is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "this is italic")

    def test_link(self):
        node = TextNode("click me", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "www.google.com"})
        self.assertEqual(html_node.value, "click me")

    def test_image(self):
        node = TextNode("img alt text", TextType.IMAGE, "good-image.com/1")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "good-image.com/1", "alt": "img alt text"})
        self.assertEqual(html_node.value, "")

    def test_other(self):
        node = TextNode("anything", None, "anything")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)





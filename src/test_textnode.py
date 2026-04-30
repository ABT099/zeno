import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_init_with_none_url_for_normal_text(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertIsNone(node.url)

    def test_init_with_none_url_for_link_text(self):
        with self.assertRaises(ValueError):
            TextNode("This is a link", TextType.LINK, None)

    def test_init_with_none_url_for_image_text(self):
        with self.assertRaises(ValueError):
            TextNode("This is an image", TextType.IMAGE, None)

    def test_repr(self):
        node = TextNode("text", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(text, bold, None)")

    def test_inequality_different_text(self):
        node1 = TextNode("text1", TextType.BOLD)
        node2 = TextNode("text2", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_plain_text_with_none_url(self):
        node = TextNode("plain text", TextType.PLAIN, None)
        self.assertEqual(node.text_type, TextType.PLAIN)

    def test_link_with_url(self):
        node = TextNode("link text", TextType.LINK, "https://example.com")
        self.assertEqual(node.url, "https://example.com")

    def test_eq_with_non_textnode(self):
        node = TextNode("text", TextType.BOLD)
        self.assertNotEqual(node, "not a textnode")

if __name__ == "__main__":
    unittest.main()
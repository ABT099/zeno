import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node

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
        node = TextNode("plain text", TextType.TEXT, None)
        self.assertEqual(node.text_type, TextType.TEXT)

    def test_link_with_url(self):
        node = TextNode("link text", TextType.LINK, "https://example.com")
        self.assertEqual(node.url, "https://example.com")

    def test_eq_with_non_textnode(self):
        node = TextNode("text", TextType.BOLD)
        self.assertNotEqual(node, "not a textnode")


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
        node = TextNode("print('Hello, world!')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('Hello, world!')")

    def test_link(self):
        node = TextNode("Click here", TextType.LINK, url="http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "http://example.com"})

    def test_image(self):
        node = TextNode("Alt text", TextType.IMAGE, url="http://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "http://example.com/image.jpg", "alt": "Alt text"})


if __name__ == "__main__":
    unittest.main()
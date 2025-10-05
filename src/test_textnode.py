import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self): 
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_different(self):
        node = TextNode("test", TextType.ITALIC, "test.com")
        node2 = TextNode("test2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_different_text(self):
        node = TextNode("This is a text node1", TextType.BOLD)
        node2 = TextNode("This is a text node2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_different_text_type(self):
        node = TextNode("test", TextType.BOLD)
        node2 = TextNode("test", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_eq_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "test.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a test", TextType.BOLD)
        print_pattern = f"TextNode({node.text}, {node.text_type.value}, {node.url})"
        self.assertEqual(node.__repr__(), print_pattern)

if __name__ == "__main__":
    unittest.main()

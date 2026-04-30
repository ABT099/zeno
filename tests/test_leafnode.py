
import unittest

from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_no_props(self):
        leaf_node = LeafNode(tag='p', value='Hello, world!', props=None)
        self.assertEqual(leaf_node.to_html(), '<p>Hello, world!</p>')

    def test_to_html_with_tag_and_props(self):
        leaf_node = LeafNode(tag='a', value='Click me!', props={'href': 'http://example.com', 'class': 'link'})
        self.assertEqual(leaf_node.to_html(), '<a href="http://example.com" class="link">Click me!</a>')

    def test_to_html_no_tag(self):
        leaf_node = LeafNode(tag=None, value='Just text', props=None)
        self.assertEqual(leaf_node.to_html(), 'Just text')

    def test_to_html_value_none_raises_error(self):
        leaf_node = LeafNode(tag='p', value=None, props=None)
        with self.assertRaises(ValueError):
            leaf_node.to_html()

    def test_to_html_empty_props(self):
        leaf_node = LeafNode(tag='div', value='Content', props={})
        self.assertEqual(leaf_node.to_html(), '<div>Content</div>')
        
if __name__ == "__main__":
    unittest.main()
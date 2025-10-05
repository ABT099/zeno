import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child", {"class": "child"})
        parent_node = ParentNode("div", [child_node], {"class": "test"})
        self.assertEqual(parent_node.to_html(), '<div class="test"><span class="child">child</span></div>')


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_no_tag(self):
        child_node = LeafNode("p", "child")
        parentnode = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parentnode.to_html()

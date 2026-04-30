import unittest
from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children(self):
        parent_node = ParentNode("div", [
            LeafNode("span", "first"),
            LeafNode("span", "second"),
            LeafNode("span", "third"),
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>first</span><span>second</span><span>third</span></div>",
        )

    def test_mixed_children_types(self):
        # Mix of LeafNodes and ParentNodes as siblings
        parent_node = ParentNode("div", [
            LeafNode("span", "leaf"),
            ParentNode("p", [LeafNode("b", "nested")]),
            LeafNode("em", "another leaf"),
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>leaf</span><p><b>nested</b></p><em>another leaf</em></div>",
        )


    def test_deep_nesting(self):
        # 4 levels deep
        node = ParentNode("div", [
            ParentNode("section", [
                ParentNode("p", [
                    ParentNode("span", [
                        LeafNode("b", "deep")
                    ])
                ])
            ])
        ])
        self.assertEqual(
            node.to_html(),
            "<div><section><p><span><b>deep</b></span></p></section></div>",
        )

    def test_multiple_children_at_every_level(self):
        node = ParentNode("div", [
            ParentNode("ul", [
                LeafNode("li", "item one"),
                LeafNode("li", "item two"),
                LeafNode("li", "item three"),
            ]),
            ParentNode("ul", [
                LeafNode("li", "item four"),
                LeafNode("li", "item five"),
            ]),
        ])
        self.assertEqual(
            node.to_html(),
            "<div>"
            "<ul><li>item one</li><li>item two</li><li>item three</li></ul>"
            "<ul><li>item four</li><li>item five</li></ul>"
            "</div>",
        )

    # --- Props / attributes ---
    def test_with_props(self):
        child_node = LeafNode("span", "hello")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>hello</span></div>',
        )

    def test_with_multiple_props(self):
        child_node = LeafNode("span", "hello")
        parent_node = ParentNode("a", [child_node], {"href": "https://example.com", "target": "_blank"})
        result = parent_node.to_html()
        # Check structure rather than prop order, as dict order can vary
        self.assertIn('href="https://example.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith("<a "))
        self.assertTrue(result.endswith("</a>"))

    def test_child_with_props(self):
        child_node = LeafNode("a", "click me", {"href": "https://example.com"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><a href="https://example.com">click me</a></div>',
        )

    def test_no_props(self):
        # Passing None explicitly for props should work the same as omitting it
        child_node = LeafNode("span", "text")
        parent_node = ParentNode("div", [child_node], None)
        self.assertEqual(parent_node.to_html(), "<div><span>text</span></div>")


    def test_empty_children_list(self):
        # An empty list is different from None — decide what your implementation should do
        parent_node = ParentNode("div", [])
        # If your implementation allows it, this should render as <div></div>
        # If not, it should raise — adjust the assertion to match your design decision
        self.assertEqual(parent_node.to_html(), "<div></div>")


    def test_leaf_child_with_no_tag(self):
        child_node = LeafNode(None, "raw text")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div>raw text</div>")

    def test_leaf_child_with_empty_string_value(self):
        child_node = LeafNode("span", "")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span></span></div>")


    def test_single_child(self):
        parent_node = ParentNode("article", [LeafNode("p", "only child")])
        self.assertEqual(parent_node.to_html(), "<article><p>only child</p></article>")


    def test_various_tags(self):
        for tag in ["section", "article", "header", "footer", "main", "nav"]:
            node = ParentNode(tag, [LeafNode("p", "text")])
            self.assertEqual(node.to_html(), f"<{tag}><p>text</p></{tag}>")


    def test_returns_string(self):
        node = ParentNode("div", [LeafNode("span", "hi")])
        self.assertIsInstance(node.to_html(), str)


if __name__ == "__main__":
    unittest.main()
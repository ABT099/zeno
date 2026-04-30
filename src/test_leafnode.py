
from src.leafnode import LeafNode

class TestLeafNode:
    def test_to_html_with_tag_no_props(self):
        leaf_node = LeafNode(tag='p', value='Hello, world!', props=None)
        assert leaf_node.to_html() == '<p>Hello, world!</p>'

    def test_to_html_with_tag_and_props(self):
        leaf_node = LeafNode(tag='a', value='Click me!', props={'href': 'http://example.com', 'class': 'link'})
        assert leaf_node.to_html() == '<a href="http://example.com" class="link">Click me!</a>'

    def test_to_html_no_tag(self):
        leaf_node = LeafNode(tag=None, value='Just text', props=None)
        assert leaf_node.to_html() == 'Just text'

    def test_to_html_value_none_raises_error(self):
        leaf_node = LeafNode(tag='p', value=None, props=None)
        try:
            leaf_node.to_html()
            assert False, "Expected ValueError"
        except ValueError as e:
            assert str(e) == "LeafNode must have a value to be rendered as HTML"

    def test_to_html_empty_props(self):
        leaf_node = LeafNode(tag='div', value='Content', props={})
        assert leaf_node.to_html() == '<div>Content</div>'
        

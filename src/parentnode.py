from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, value=None, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must contain a tag")
        if not self.children or len(self.children) == 0:
            raise ValueError("Parent node must have atleast 1 child")

        html_props = self.props_to_html()
        result = f"<{self.tag}{html_props}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result


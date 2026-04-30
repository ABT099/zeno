
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to be rendered as HTML")
        
        if self.children is None:
            raise ValueError("ParentNode must have children to be rendered as HTML")
        
        result = f"<{self.tag}"
        result += self.props_to_html()
        result += ">"

        for child in self.children:
            result += child.to_html()

        result += f"</{self.tag}>"

        return result

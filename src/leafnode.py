
from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a value to be rendered as HTML")
        
        if self.tag is None:
            return self.value
        
        props_html = self.props_to_html().strip()
        if props_html:
            result = f'<{self.tag} {props_html}>'
        else:
            result = f'<{self.tag}>'
        result += f'{self.value}</{self.tag}>'
        return result        
    
    def __repr__(self) -> str:
        return f'LeafNode(tag="{self.tag}", value="{self.value}", props="{self.props}")'
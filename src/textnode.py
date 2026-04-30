from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type

        if (text_type == TextType.LINK or text_type == TextType.IMAGE) and url is None:
            raise ValueError(f"URL must be provided for text type {text_type.value}")

        self.url = url

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, TextNode):
            return False
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self) -> str:
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'
    

    

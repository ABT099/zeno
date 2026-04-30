
class HTMLNode:
    def __init__(self, tag: str | None, value: str | None, children: list["HTMLNode"] | None, props: dict[str, str] | None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method must be implemented by child classes to override it to render themselves as HTML")
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        res = ""
        idx = 1

        for k, v in self.props.items():
            res += f'{k}="{v}"'

            if (idx != len(self.props)):
                res += " "
                idx += 1

        return res
    
    def __repr__(self) -> str:
        return f'HTMLNode(tag="{self.tag}", value="{self.value}", children="{self.children}", props="{self.props}")'

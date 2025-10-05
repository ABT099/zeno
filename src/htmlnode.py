class HTMLNode:

    """
        - tag: A string representing the HTML tag name (e.g. 'p', 'a', 'h1', etc.)
        - value: A string representing the value inside the HTML tag
        - children: A list of HTMLNode objects representing the children of this node
        - props: A dictionary representing attributes of an HTML tag, example: a link '<a>' might have an 'href="www.google.com".

        All the values here are optional, an HTMLNode without a tag will render just text, and so on, it will better reflect how html work
    """
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result = ""
        if self.props:
            for k, v in self.props.items():
                result += f' {k}="{v}"'
        return result

    def __repr__(self):
        return f"tag: <{self.tag}>\nprops: {self.props_to_html()}\nvalue: {self.value}"


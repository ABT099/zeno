
from src.textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list["TextNode"]:
    new_nodes = []    
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown: no closing '{delimiter}' delimiter in: {node.text!r}")
        
        for i, part in enumerate(parts):
                if part == "":
                    continue  # skip empty strings from leading/trailing delimiters
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))

    return new_nodes
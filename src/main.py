

from src.inline_markdown import split_nodes_image
from src.leafnode import LeafNode
from src.parentnode import ParentNode
from src.textnode import TextNode, TextType

def main():
    
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    res = node.to_html()
    print(res)

if __name__ == "__main__":
    main()
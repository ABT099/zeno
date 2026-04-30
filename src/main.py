

from leafnode import LeafNode
from parentnode import ParentNode

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
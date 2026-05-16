import re

from src.textnode import TextType, TextNode

_URL = r'[^\s()]+(?:\([^\s()]*\)[^\s()]*)*'

IMAGE_PATTERN = re.compile(rf'!\[([^\[\]]*)\]\(({_URL})\)')
LINK_PATTERN  = re.compile(rf'(?<!!)\[([^\[\]]*)\]\(({_URL})\)')


def text_to_textnodes(text) -> list[TextNode]:
    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

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

# returns a list of tuples (alt_text, image_url)
def extract_markdown_images(markdown: str):
    image_texts = IMAGE_PATTERN.findall(markdown)
    results = []
    for alt_text, image_url in image_texts:
        results.append((alt_text, image_url))
    return results

# returns a list of tuples (anchor_text, link_url)
def extract_markdown_links(markdown: str):
    link_texts = LINK_PATTERN.findall(markdown)
    results = []
    for anchor_text, link_url in link_texts:
        results.append((anchor_text, link_url))
    return results

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if not images:
            new_nodes.append(node)
            continue

        text = node.text
        for image_alt, image_link in images:
            sections = text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, url=image_link))
            text = sections[1]

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue

        text = node.text
        for anchor_text, link_url in links:
            sections = text.split(f"[{anchor_text}]({link_url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url=link_url))
            text = sections[1]
        
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
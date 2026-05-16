
import unittest

from src.inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from src.textnode import TextNode, TextType
from src.inline_markdown import extract_markdown_images
from src.inline_markdown import extract_markdown_links

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://me.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://me.dev"),
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_textnodes_plain_text(self):
        nodes = text_to_textnodes("This is plain text.")
        expected = [
            TextNode("This is plain text.", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_textnodes_adjacent_styles(self):
        nodes = text_to_textnodes("**bold**_italic_`code`")
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_textnodes_repeated_same_style_spans(self):
        nodes = text_to_textnodes("This has **first** and **second** bold words.")
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("first", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("second", TextType.BOLD),
            TextNode(" bold words.", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_textnodes_images_and_links(self):
        nodes = text_to_textnodes(
            "An ![image](https://example.com/img.png) and a [link](https://example.com)"
        )
        expected = [
            TextNode("An ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_textnodes_urls_with_parentheses(self):
        nodes = text_to_textnodes(
            "An ![image](https://example.com/img(1).png) and a [link](https://example.com/page(1).html)"
        )
        expected = [
            TextNode("An ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img(1).png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com/page(1).html"),
        ]
        self.assertEqual(nodes, expected)

    def test_text_to_textnodes_unmatched_bold_raises(self):
        with self.assertRaises(ValueError):
            text_to_textnodes("This has **unclosed bold")

    def test_text_to_textnodes_unmatched_code_raises(self):
        with self.assertRaises(ValueError):
            text_to_textnodes("This has `unclosed code")

    def test_text_to_textnodes_does_not_process_markup_inside_non_text_nodes(self):
        nodes = text_to_textnodes("Use **![image](https://example.com/img.png) and [link](https://example.com)** here")
        expected = [
            TextNode("Use ", TextType.TEXT),
            TextNode(
                "![image](https://example.com/img.png) and [link](https://example.com)",
                TextType.BOLD,
            ),
            TextNode(" here", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_split_nodes_delimiter_bold(self):
        nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_italic(self):
        nodes = [TextNode("This is *italic* text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_code(self):
        nodes = [TextNode("This is `code` text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_unmatched(self):
        nodes = [TextNode("This is **bold text", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    def test_extract_markdown_images(self):
        markdown = "Here is an image: ![alt text](http://example.com/image.png) and another one ![another image](http://example.com/image2.png)"
        result = extract_markdown_images(markdown)
        expected = [
            ("alt text", "http://example.com/image.png"),
            ("another image", "http://example.com/image2.png")
        ]
        self.assertEqual(result, expected)

    def test_extract_markdown_images_with_parentheses_in_url(self):
        markdown = "Here is an image: ![alt text](http://example.com/image(1).png)"
        result = extract_markdown_images(markdown)
        expected = [
            ("alt text", "http://example.com/image(1).png")
        ]
        self.assertEqual(result, expected)

    def test_extract_markdown_images_no_images(self):
        markdown = "This is a text without images."
        result = extract_markdown_images(markdown)
        expected = []
        self.assertEqual(result, expected)

    def test_extract_markdown_links(self):
        markdown = "Here is a link: [Google](https://www.google.com) and another one [GitHub](https://github.com)"
        result = extract_markdown_links(markdown)
        expected = [
            ("Google", "https://www.google.com"),
            ("GitHub", "https://github.com")
        ]
        self.assertEqual(result, expected)

    def test_extract_markdown_links_with_parentheses_in_url(self):
        markdown = "Here is a link: [Example](https://example.com/path_(1).html)"
        result = extract_markdown_links(markdown)
        expected = [
            ("Example", "https://example.com/path_(1).html")
        ]
        self.assertEqual(result, expected)

    def test_extract_markdown_links_no_links(self):
        markdown = "This is a text without links."
        result = extract_markdown_links(markdown)
        expected = []
        self.assertEqual(result, expected)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_return_original_when_no_image(self):
        node = TextNode("This is a text without an image", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("This is a text without an image", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_images_preserves_trailing_text(self):
        node = TextNode(
            "before ![image](https://example.com/img.png) after",
            TextType.TEXT,
        )
        self.assertEqual(split_nodes_image([node]), [
            TextNode("before ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" after", TextType.TEXT),
        ])


    def test_split_images_preserves_text_nodes_without_images(self):
        nodes = [
            TextNode("plain text", TextType.TEXT),
            TextNode("![img](https://example.com/img.png)", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_image(nodes), [
            TextNode("plain text", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://example.com/img.png"),
        ])


    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://google.com) and another [second link](https://youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://youtube.com"
                ),
            ],
            new_nodes,
        )

    def test_split_links_return_original_when_no_link(self):
        node = TextNode("This is a text without a link", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is a text without a link", TextType.TEXT)
            ],
            new_nodes
        )
        
    def test_split_links_preserves_trailing_text(self):
        node = TextNode(
            "before [link](https://example.com) after",
            TextType.TEXT,
        )
        self.assertEqual(split_nodes_link([node]), [
            TextNode("before ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" after", TextType.TEXT),
        ])


if __name__ == '__main__':
    unittest.main()

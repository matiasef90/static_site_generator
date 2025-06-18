from util import split_nodes_delimiter, extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType
import unittest

class TestParentNode(unittest.TestCase):
    def test_split_nodes_delimiter_base(self):
        result = split_nodes_delimiter(
            [TextNode("This is text with a `code block` word", TextType.TEXT)],
            "`",
            TextType.CODE
        )
        shouldBy = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(result, shouldBy)
    
    def test_split_nodes_delimiter_raise(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter("text base", "TT", TextType.ITALIC)

    def test_split_nodes_delimiter_italic(self):
        test = split_nodes_delimiter(
            [
                TextNode("_italic_ text para gente _italiana_", TextType.TEXT),
                TextNode("un texto _italic_ por aca _fin_", TextType.TEXT)
            ], "_", TextType.ITALIC
        )
        spected = [
            TextNode("italic", TextType.ITALIC),
            TextNode(" text para gente ", TextType.TEXT),
            TextNode("italiana", TextType.ITALIC),
            TextNode("un texto ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" por aca ", TextType.TEXT),
            TextNode("fin", TextType.ITALIC),
        ]
        self.assertEqual(test, spected)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
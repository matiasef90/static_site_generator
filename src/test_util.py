from util import *
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

    def test_split_nodes_link_one(self):
        output = split_nodes_link([TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
             TextType.TEXT
        )])
        expect_output = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(output, expect_output)
    
    def test_split_nodes_link_two(self):
        output = split_nodes_link([TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
             TextType.TEXT
        )])
        expect_output = [
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(output, expect_output)

    def test_split_nodes_link_three(self):
        output = split_nodes_link([
            TextNode("hola [ms1](url1) world", TextType.TEXT),
            TextNode("[ms2](url2) world", TextType.TEXT),
            TextNode("hola [ms3](url3)", TextType.TEXT),
        ])
        expect_output = [
            TextNode("hola ", TextType.TEXT),
            TextNode("ms1", TextType.LINK, "url1"),
            TextNode(" world", TextType.TEXT),
            TextNode("ms2", TextType.LINK, "url2"),
            TextNode(" world", TextType.TEXT),
            TextNode("hola ", TextType.TEXT),
            TextNode("ms3", TextType.LINK, "url3"),
        ]
        self.assertListEqual(output, expect_output)
    def test_split_nodes_image_one(self):
        output = split_nodes_images([TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
             TextType.TEXT
        )])
        expect_output = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(output, expect_output)
    
    def test_split_nodes_image_two(self):
        output = split_nodes_images([TextNode(
            "![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
             TextType.TEXT
        )])
        expect_output = [
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(output, expect_output)

    def test_split_nodes_image_three(self):
        output = split_nodes_images([
            TextNode("hola ![ms1](url1) world", TextType.TEXT),
            TextNode("![ms2](url2) world", TextType.TEXT),
            TextNode("hola ![ms3](url3)", TextType.TEXT),
        ])
        expect_output = [
            TextNode("hola ", TextType.TEXT),
            TextNode("ms1", TextType.IMAGE, "url1"),
            TextNode(" world", TextType.TEXT),
            TextNode("ms2", TextType.IMAGE, "url2"),
            TextNode(" world", TextType.TEXT),
            TextNode("hola ", TextType.TEXT),
            TextNode("ms3", TextType.IMAGE, "url3"),
        ]
        self.assertListEqual(output, expect_output)
    
    def test_text_to_node(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expect = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_node(text), expect)
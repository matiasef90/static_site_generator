import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        self.assertEqual(node, node2)
    
    def test_not_eq_type(self):
        node = TextNode("One node", TextType.ITALIC)
        node2 = TextNode("One node", TextType.CODE)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_url(self):
        node = TextNode("One node", TextType.CODE, "google.com")
        node2 = TextNode("One node", TextType.CODE)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_text(self):
        node = TextNode("One node 1", TextType.CODE)
        node2 = TextNode("One node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
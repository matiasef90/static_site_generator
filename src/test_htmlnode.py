import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_create_None(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_create_p(self):
        node = HTMLNode("p", "texto interno")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "texto interno")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_create_props(self):
        node = HTMLNode("p", "texto", None, {"color": "red"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "texto")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"color": "red"})

if __name__ == "__main__":
    unittest.main()
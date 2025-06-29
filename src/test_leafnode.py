import unittest
from leafnode import LeafNode

class TestLeafNone(unittest.TestCase):
    def test_leaf_node_p(self):
        node = LeafNode("p", "Hello, world!!")
        self.assertEqual(node.to_html(), "<p>Hello, world!!</p>")
    
    def test_leaf_node_h1(self):
        node = LeafNode("h1", "Hello, world!!", {"color": "red", "size": 26})
        self.assertEqual(node.to_html(), '<h1 color="red" size="26">Hello, world!!</h1>')
    
    def test_leaf_node_no_tag(self):
        node = LeafNode(None, "Hello, world!!")
        self.assertEqual(node.to_html(), 'Hello, world!!')
    
    def test_leaf_node_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

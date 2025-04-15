import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_children_and_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"p1":"one", "p2":"two"})
        self.assertEqual(parent_node.to_html(), "<div p1=\"one\" p2=\"two\"><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
   
    def test_to_html_with_grandgrandchildren(self):
        grandgrandchild_node = LeafNode("a", "grandgrandchild")
        grandchild_node = ParentNode("b", [grandgrandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><a>grandgrandchild</a></b></span></div>",
        )
    
    def test_to_html_without_tag(self):
        child_node = ParentNode("span", "childnode")
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError)
    
    def test_to_html_without_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError)
    
    def test_to_html_without_children_two(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError)
import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
     node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
     node2 = HTMLNode("")
     node3 = HTMLNode(props={"class": "btn"})
     self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"',)
     self.assertEqual(node2.props_to_html(), "")
     self.assertEqual(node3.props_to_html(), ' class="btn"')
     
    def test_leaf_to_html_p(self):
     node = LeafNode("p", "Hello, world!")
     self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
if __name__ == "__main__":
    unittest.main()
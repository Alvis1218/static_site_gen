import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node
)
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_var_text(self):
        node = TextNode("One of us always tells the truth", "italic", "https://www.boot.dev")
        node2 = TextNode("And the other always lies", "italic", "https://www.boot.dev")
        self.assertNotEqual(node, node2)
    
    def test_text_to_HTML(self):
        node = LeafNode("b", "Why hello there")
        node2 = text_node_to_html_node(TextNode("Why hello there", text_type_bold))
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()

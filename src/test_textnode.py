import unittest
from textnode import TextNode
from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href":text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")

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

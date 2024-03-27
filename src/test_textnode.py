import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_urlNone(self):
        node = TextNode("This is a text node", "italic", "None")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    
    def test_var_text(self):
        node = TextNode("One of us always tells the truth", "italic", "https://www.boot.dev")
        node2 = TextNode("And the other always lies", "italic", "https://www.boot.dev")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

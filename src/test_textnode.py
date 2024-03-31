import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2, "The two nodes are not the exact same")
    
    def test_eq_false(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2, "The two nodes are the same, should not be.")
    
    def test_eq_false2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is not a text node", "bold")
        self.assertNotEqual(node, node2, "The two nodes are the same, should not be.")
    
    def test_eq_url(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertEqual(node, node2, "The two nodes have similar urls and other properties")

    def test_repr(self):
        node = TextNode("this is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(f"TextNode(this is a text node, bold, https://www.boot.dev)", repr(node), "The string format is not the same")


if __name__ == "__main__":
    unittest.main()
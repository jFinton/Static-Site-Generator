import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a HTML node", None, {"class": "greeting", "href": "https://www.boot.dev"})
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://www.boot.dev"'
        )
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello!")
        self.assertEqual(node.to_html(), "<p>Hello!</p>")
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello Everyone!")
        self.assertEqual(node.to_html(), "Hello Everyone!")


if __name__ == "__main__":
    unittest.main()
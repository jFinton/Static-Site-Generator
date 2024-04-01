import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_parent_to_html(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_parent_with_parent_to_html(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold Text"),
                        LeafNode(None, "Normal Text")
                    ],
                ),
                LeafNode("i", "italic text")
            ],
            { "class": "annoying"}
        )
        self.assertEqual(node.to_html(), '<div class="annoying"><p><b>Bold Text</b>Normal Text</p><i>italic text</i></div>')


if __name__ == "__main__":
    unittest.main()
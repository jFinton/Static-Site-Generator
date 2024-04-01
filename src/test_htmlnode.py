import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a HTML node", None, {"class": "greeting", "href": "https://www.boot.dev"})
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://www.boot.dev"'
        )


if __name__ == "__main__":
    unittest.main()
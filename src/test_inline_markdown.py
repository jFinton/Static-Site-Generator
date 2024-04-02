import unittest
from inline_markdown import (split_nodes_delimiter,  split_nodes_image,  
                             split_nodes_link, extract_markdown_images, 
                             extract_markdown_links, text_to_textnodes)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )
    
    def test_extract_image(self):
        text = "This is an ![image](https://www.abc.com) and then there is ![bigger_image](https://cartoons.com)"
        result = [("image", "https://www.abc.com"), ("bigger_image", "https://cartoons.com")]
        self.assertListEqual(
            extract_markdown_images(text),
            result
        )
    
    def test_extract_link(self):
        text = "This is a [link](https://www.hello.com) which has another link called [another](https://starsandplanets.com)"
        result = [("link", "https://www.hello.com"), ("another", "https://starsandplanets.com")]
        self.assertListEqual(
            extract_markdown_links(text),
            result
        )

    def test_split_image(self):
        node = TextNode("This is a single ![image](https://www.image.com)", text_type_text)
        result = [
            TextNode("This is a single ", text_type_text),
            TextNode("image", text_type_image, "https://www.image.com")
        ]
        self.assertListEqual(
            split_nodes_image([node]),
            result
        )

    def test_split_multi_images(self):
        nodes = [
            TextNode("This is a single ![image](https://www.image.com)", text_type_text),
            TextNode("Bolded One", text_type_bold),
            TextNode("This has 2 ![image](https://www.firstone.com) because I am that ![crazy](https://www.second.com) the end.", text_type_text),
            TextNode("Sample Text", text_type_text)
        ]
        result = [
            TextNode("This is a single ", text_type_text),
            TextNode("image", text_type_image, "https://www.image.com"),
            TextNode("Bolded One", text_type_bold),
            TextNode("This has 2 ", text_type_text),
            TextNode("image", text_type_image, "https://www.firstone.com"),
            TextNode(" because I am that ", text_type_text),
            TextNode("crazy", text_type_image, "https://www.second.com"),
            TextNode(" the end.", text_type_text),
            TextNode("Sample Text", text_type_text)
        ]
        self.assertListEqual(
            split_nodes_image(nodes),
            result
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            split_nodes_link([node])
        )

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        result = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev")
        ]
        self.assertListEqual(
            text_to_textnodes(text),
            result
        )


if __name__ == "__main__":
    unittest.main()
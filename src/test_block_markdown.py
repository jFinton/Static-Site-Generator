import unittest

from block_markdown import (markdown_to_blocks, block_to_block_type,
                            markdown_to_html)
from block_markdown import (
    block_type_paragraph,
    block_type_code,
    block_type_heading,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list
)


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        results = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        self.assertListEqual(
            markdown_to_blocks(markdown),
            results
        )
    

    def test_markdown_to_multi_blocks(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items


"""
        results = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        self.assertListEqual(
            markdown_to_blocks(markdown),
            results
        )


    def test_block_to_block_type(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "#### This is another heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "###I am tricking"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "> This is a quote\n> of multiple lines"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = ">Tricking you again"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "* This is a list\n* of unorderedness"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "- This is another\n- list of unorderedness"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "* I am random\n- of all accounts"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "1. I am a list\n2. of orderedness"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "1. Single line list"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "1. I am just random\n4. if everything is odd"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "I am test to trick you, not really"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)


    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()
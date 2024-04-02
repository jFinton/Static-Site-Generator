from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    results = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            results.append(node)
        else:
            texts = node.text.split(delimiter)
            if len(texts) % 2 == 0:
                raise Exception(f"Invalid Markdown Syntax: Check for matching delimiter in {node.text}")
            else:
                for i in range(len(texts)):
                    if texts[i] == "":
                        continue
                    if i % 2 == 0:
                        results.append(TextNode(texts[i], text_type_text))
                    else:
                        results.append(TextNode(texts[i], text_type))
    return results


def extract_markdown_images(text):
    pass


def extract_markdown_links(text):
    pass
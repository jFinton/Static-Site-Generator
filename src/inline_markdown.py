from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

import re

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


def split_nodes_image(old_nodes):
    results = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            results.append(node)
            continue
        text = node.text
        image_tups = extract_markdown_images(text)
        if not image_tups:
            results.append(node)
            continue
        for image_tup in image_tups:
            sections = text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if len(sections) != 2:
                raise Exception(f"Invalid Syntax: Image not closed for {image_tup}")
            if sections[0] != "":
                results.append(TextNode(sections[0], text_type_text))
            results.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
            text = sections[1]
        if text != "":
            results.append(TextNode(text, text_type_text))
    return results




def split_nodes_link(old_nodes):
    results = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            results.append(node)
            continue
        text = node.text
        link_tups = extract_markdown_links(text)
        if not link_tups:
            results.append(node)
            continue
        for link_tup in link_tups:
            sections = text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if len(sections) != 2:
                raise Exception(f"Invalid Syntax: Link not closed for {link_tup}")
            if sections[0] != "":
                results.append(TextNode(sections[0], text_type_text))
            results.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
            text = sections[1]
        if text != "":
            results.append(TextNode(text, text_type_text))
    return results



def extract_markdown_images(text):
    result = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return result


def extract_markdown_links(text):
    result = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return result

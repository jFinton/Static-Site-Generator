from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode

def main():
    test_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(test_node)

main()
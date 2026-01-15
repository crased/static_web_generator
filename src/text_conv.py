from htmlnode import LeafNode,HTMLNode
from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images, extract_markdown_links
from split_nodes import split_nodes_images, split_nodes_links
from delimiter import split_nodes_delimiter
def text_to_textnodes(text):
    result = []
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`", TextType.CODE)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes
from textnode import TextNode, TextType,text_node_to_html_node
from htmlnode import HTMLNode
from text_conv import text_to_textnodes


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children_html_nodes = []
    for node in text_nodes:
        children_html_nodes.append(text_node_to_html_node(node))
    return children_html_nodes    
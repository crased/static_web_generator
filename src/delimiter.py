from htmlnode import LeafNode,HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.TEXT:
            sections = old_node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception("error invalid markdown syntax")
            temp_list = []
            for i, section in enumerate(sections):
               if section == "":
                  continue
               if i % 2 == 0:
                  node = TextNode(section,TextType.TEXT)
               else:  
                  node = TextNode(section,text_type)
               temp_list.append(node)
            new_node.extend(temp_list)
        else:
            new_node.append(old_node) 
        
    return new_node
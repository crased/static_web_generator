from htmlnode import LeafNode,HTMLNode
from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images, extract_markdown_links
def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
           new_nodes.append(old_node)
           continue 
        links = extract_markdown_images(old_node.text)
        if len(links) == 0:
           new_nodes.append(old_node)  
           continue
        remaining_text = old_node.text
        for image_alt, image_link in links:
          sections = remaining_text.split(f"![{image_alt}]({image_link})",1)
          before = sections[0]
          after = sections[1]
          if before != "":
              new_nodes.append(TextNode(before, TextType.TEXT))
          new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
          remaining_text = after
        if remaining_text != "":
          new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes      
def split_nodes_links(old_nodes):    
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
           new_nodes.append(old_node)
           continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
           new_nodes.append(old_node)
           continue
        remaining_text = old_node.text
        for link_text, link_url in links:
            sections = remaining_text.split(f"[{link_text}]({link_url})",1)
            before = sections[0]
            after = sections[1]
            if before != "":
              new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))    
            remaining_text = after
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes             
              
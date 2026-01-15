from markdown_block import markdown_to_blocks, block_to_block_type
from get_heading_tag import heading_tag
from blocknode import BlockType
from text_to_child import text_to_children
import textnode
from htmlnode import HTMLNode, ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    temp = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
           tag = "p"
           children_nodes = text_to_children(block)
           ht_nodes = ParentNode(tag=tag,children=children_nodes)
           temp.append(ht_nodes)
        elif block_type == BlockType.HEADING:
           tag = heading_tag(block)
           heading_cont = block.lstrip("#").lstrip()
           children_nodes = text_to_children(heading_cont)
           ht_nodes = ParentNode(tag=tag,children=children_nodes)
           temp.append(ht_nodes)
        elif block_type == BlockType.CODE:
           code_text = block.strip("`")
           code_text_node = TextNode(code_text, TextType.CODE)
           inner_code = text_node_to_html_node(code_text_node)         
           ht_nodes = ParentNode("pre",children=[inner_code])
           temp.append(ht_nodes)
        elif block_type == BlockType.UNORDERED_LIST:
           lines = block.split("\n")
           li_nodes = []
           for line in lines:
             item_text = line.strip()[2:]  # remove "- "
             children = text_to_children(item_text)
             li_nodes.append(ParentNode("li", children))
           ht_nodes = ParentNode("ul", li_nodes)
           temp.append(ht_nodes)
        elif block_type == BlockType.ORDERED_LIST:
           lines = block.split("\n")
           li_nodes = []
           for line in lines:
             stripped = line.strip()
             item_text = stripped.split(". ", 1)[1]  # remove "1. ", "2. ", etc.
             children = text_to_children(item_text)
             li_nodes.append(ParentNode("li", children))
           ht_nodes = ParentNode("ol", li_nodes)
           temp.append(ht_nodes)
        elif block_type == BlockType.QUOTE:
           lines = block.split("\n")
           stripped_lines = []
           for line in lines:
             s = line.lstrip()
             if s.startswith("> "):
               s = s[2:]
             elif s.startswith(">"):
               s = s[1:]
             stripped_lines.append(s)
           quote_text = "\n".join(stripped_lines).strip()
           children = text_to_children(quote_text)
           ht_nodes = ParentNode("blockquote", children)
           temp.append(ht_nodes) 
        else:
            raise ValueError(f"Unknown block type: {block_type}")
    div_node = ParentNode(tag="div", children=temp)   
    return div_node
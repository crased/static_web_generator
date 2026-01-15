from markdown_to_html import markdown_to_html_node
from get_title import extract_title
from pathlib import Path
import htmlnode
import os
def generate_page(from_path, template_path, dest_path):
    print(f"this could take some time, initilizing!! :{from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as file:
        markdown = file.read()
    with open(template_path,"r", encoding="utf-8") as file:    
        template = file.read()
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}",title)
    page = page.replace("{{ Content }}",html)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(page)
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content,entry)
        dest_path_lg = os.path.join(dest_dir_path, entry)
        if os.path.isfile(src_path):
           if entry.lower().endswith(".md"):
             html_dest = Path(dest_path_lg).with_suffix(".html")
             generate_page(src_path,template_path,html_dest)
        else:
            generate_pages_recursive(src_path,template_path, dest_path_lg)
    
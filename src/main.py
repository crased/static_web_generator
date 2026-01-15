from textnode import TextNode, TextType
from page_gen import generate_page, generate_pages_recursive
import os 
import shutil


def copy_static(src,dst):
    if os.path.exists(src):
       for file_name in os.listdir(src):
          src_path = os.path.join(src,file_name)
          dst_path = os.path.join(dst,file_name)
          if os.path.isfile(src_path):
            shutil.copy(src_path,dst_path)
          else:
            os.mkdir(dst_path)
            copy_static(src_path,dst_path)
def main():
 if os.path.exists("public"):
    shutil.rmtree("public") 
 os.mkdir("public")   
 copy_static("static","public") 
 generate_pages_recursive("content",
                          "template.html",
                          "public",)       



if __name__ == "__main__":
   main()
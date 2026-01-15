from textnode import TextNode, TextType
from page_gen import generate_page, generate_pages_recursive
import os 
import shutil
import sys

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
 if len(sys.argv) > 1:   
    basepath = sys.argv[1]
 else:
    basepath = "/"   
 if os.path.exists("docs"):
    shutil.rmtree("docs") 
 os.mkdir("docs")   
 copy_static("static","docs") 
 generate_pages_recursive("content",
                          "template.html",
                          "docs",basepath)       



if __name__ == "__main__":
   main()
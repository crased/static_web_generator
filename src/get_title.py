
from get_heading_tag import heading_tag
def extract_title(markdown):
    for line in markdown.split("\n"):
      if heading_tag(line) == "h1":
       temp_mk = line.lstrip("#").strip()
       return temp_mk
    else:
        raise Exception("no header found!")
    
import blocknode
import markdown
def heading_tag(block):
    line = block.split("\n")[0]
    result = 0
    for char in line:
      if char == "#":
        result += 1
      else:
        break
    if result == 1:
       return "h1"
    if result == 2:
       return "h2"
    if result == 3:
       return "h3"
    if result == 4:
       return "h4"
    if result == 5:
       return "h5"
    if result == 6:
       return "h6"               

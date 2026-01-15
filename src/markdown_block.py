from blocknode import BlockType


def markdown_to_blocks(markdown):
    rg_block = markdown.split("\n\n")
    blocks = []
    for block in rg_block:
        clean = block.strip()
        if not clean:
          continue
        blocks.append(clean)
    return blocks    

def block_to_block_type(block: str):
    line = block.split("\n")[0]
    result = 0
    for char in line:
      if char == "#":
        result += 1
      else:
        break
    if 1 <= result and result <= 6 and len(line) > result and line[result] == " ":
      return BlockType.HEADING
    lines = block.split("\n")
    if all(l.strip().startswith("- ") for l in lines):  
       return BlockType.UNORDERED_LIST
    if list_order(block):
      return BlockType.ORDERED_LIST
    if all(l.strip().startswith(">") for l in lines):
      return BlockType.QUOTE
    return BlockType.PARAGRAPH  


def list_order(block):
    lines = block.split("\n")
    for line in lines:
        stripped = line.lstrip()
        parts = stripped.split(". ", 1)
        if len(parts) != 2:
            return False
        number_str, _ = parts
        if not number_str.isdigit():
            return False
    return True  

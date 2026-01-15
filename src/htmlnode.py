
class HTMLNode:

 def __init__(self,tag=None,value=None,children=None,props=None):
  self.tag = tag
  self.value = value
  self.children = children
  self.props = props   

 def to_html(self):
  raise NotImplementedError("override")
 def props_to_html(self):
    if not self.props:
       return ""
    else:   
     result = ""
     for key,value in self.props.items():
       result = result + f' {key}="{value}"'
     return result
 def __repr__(self):
    return f"Tag{self.tag}: Value{self.value}: Children{self.children}: Props{self.props}"
class LeafNode(HTMLNode):  

  def __init__(self,tag,value,props=None): 
     super().__init__(tag,value,None,props)

  def to_html(self):   
   if self.value is None:
      raise ValueError("all LeafNodes must have a value!")
   if self.tag is None:
      return self.value   
   else:
      return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
class ParentNode(HTMLNode):      

  def __init__(self,tag,children,props=None): 
      super().__init__(tag,None,children,props)

  def to_html(self):
   if self.tag is None:
      raise ValueError("all ParentNodes must have a value!")
   if self.children is None:
      raise ValueError("missing children!")
   else:
     kids = ""
     for child in self.children:
        kids = kids + child.to_html() 
     return f"<{self.tag}{self.props_to_html()}>{kids}</{self.tag}>"
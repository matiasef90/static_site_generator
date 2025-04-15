from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("tag are required")
        if self.children == None or len(self.children) == 0:
            raise ValueError("One child is at least required")
        props = ""
        if self.props != None:
            for key, val in self.props.items():
                props += f' {key}="{val}"'
        childrens = ""
        for c in self.children:
            childrens += c.to_html()
        return f"<{self.tag}{props}>{childrens}</{self.tag}>"
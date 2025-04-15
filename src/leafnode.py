from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value most be provided")
        if self.tag == None:
            return self.value
        props = ""
        if self.props != None:
            for key, val in self.props.items():
                props += f' {key}="{val}"'
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
    
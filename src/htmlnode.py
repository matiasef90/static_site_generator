
class HTMLNode():
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        array_props = []
        try:
            for key, val in self.props.items():
                array_props.append(f'{key}="{value}"')
            return " ".join(array_props)
        except:
            raise Exception("props are None")
            
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"

    
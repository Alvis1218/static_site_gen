class HTMLNode:
    def __init__(self, TAG=None, VALUE=None, CHILDREN=None, PROPS=None):
        self.tag = TAG
        self.value = VALUE
        self.children = CHILDREN
        self.props = PROPS
    
    def to_html(self):
        raise NotImplementedError("to_html method not inplemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        attributes = ""
        for key in self.props:
            attributes += f' {key}="{self.props[key]}"'
        return attributes
    
    def __repr__(self):
        return f"HTMLNode(TAG={self.tag}, VALUE={self.value}, CHILDREN={self.children}, PROPS={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, TAG, VALUE, PROPS=None):
        super().__init__(TAG, VALUE, None, PROPS)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(TAG={self.tag}, VALUE={self.value}, PROPS={self.props})"
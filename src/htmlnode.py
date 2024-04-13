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
    
    def __eq__(self, other):
        if (self.tag == other.tag) and (self.value == other.value) and (self.children == other.children) and (self.props == other.props):
            return True
        return False
    
    def __repr__(self):
        return f"HTMLNode(TAG : {self.tag}, VALUE : {self.value}, CHILDREN : {self.children}, PROPS : {self.props})"

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
        return f"LeafNode(TAG : {self.tag}, VALUE : {self.value}, PROPS : {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, TAG, CHILDREN, PROPS=None):
        super().__init__(TAG, None, CHILDREN, PROPS)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes require a tag")
        if self.children is None:
            raise ValueError("All parent nodes require at least one child")
        all_children_html = ""
        for child in self.children:
            all_children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{all_children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(TAG : {self.tag}, CHILDREN : {self.children}, PROPS : {self.props})"
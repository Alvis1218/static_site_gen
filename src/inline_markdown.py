from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError(f"No closing {delimiter} delimiter found")
        for idx, text_content in enumerate(split_text):
            if text_content == "":
                continue
            if idx % 2 == 0:
                new_nodes.append(TextNode(text_content, text_type_text))
            else:
                new_nodes.append(TextNode(text_content, text_type))
    return new_nodes
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    validDelimiter = ["`", "_", "**"]
    if delimiter not in validDelimiter:
        raise Exception("invalid markdown syntax")
    newNodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            newNodes.append(node)
            continue
        elements = node.text.split(delimiter)
        for i in range(len(elements)):
            if elements[i] == "":
                continue
            if i % 2 == 0 and elements[i]:
                newNodes.append(TextNode(elements[i], TextType.TEXT))
            else:
                newNodes.append(TextNode(elements[i], text_type))
    return newNodes
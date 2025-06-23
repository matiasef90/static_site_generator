from textnode import TextNode, TextType
import re

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

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_link(nodes):
    new_nodes = []
    for node in nodes:
        text = node.text
        links = extract_markdown_links(text)
        text = re.sub(r"\[(.*?)\]\((.*?)\)", "_link_", text)
        text = text.split("_")
        index_link = 0
        for sub_text in text:
            if sub_text == "":
                continue
            if sub_text == "link":
                tag, url = links[index_link]
                new_nodes.append(TextNode(tag, TextType.LINK, url))
                index_link+=1
                continue
            new_nodes.append(TextNode(sub_text, TextType.TEXT))
    return new_nodes

def split_nodes_images(nodes):
    new_nodes = []
    for node in nodes:
        text = node.text
        images = extract_markdown_images(text)
        text = re.sub(r"\!\[(.*?)\]\((.*?)\)", "_images_", text)
        text = text.split("_")
        index_images = 0
        for sub_text in text:
            if sub_text == "":
                continue
            if sub_text == "images":
                tag, url = images[index_images]
                new_nodes.append(TextNode(tag, TextType.IMAGE, url))
                index_images+=1
                continue
            new_nodes.append(TextNode(sub_text, TextType.TEXT))
    return new_nodes
    
# Name: Siyuan Yan
# ID: 28498704

"""calculate the frequency of each character in the text"""
def calculate_Frequency(text):
    """
    :param text
    :return: a dict that key is character, val is the character's frequency
    """
    dict={}
    for char in text:
        if char not in dict:
            dict[char]=1
        else:
            dict[char]+=1
    return dict

class Node:
    def __init__(self):
        self.freq=0
        self.name=None
        self.l=None
        self.r=None
        self.code=''

"""buil a huffman binary tree to generate prefix-free codes"""
def buildHuffmanTree(dict):
    node_list=[]
    node = Node()
    for i in dict:
        node=Node()
        node.name=i
        node.freq=dict[i]
        node_list.append(node)
    if len(node_list)==1:
        encode_dict[node.name] = '0'
        decode_dict['0'] = node.name

        return node
    # if len(node_list)<=1:
    #     merged_node=node
    merged_node=Node
    while len(node_list)>1:
        node_list.sort(reverse=True,key=lambda node:node.freq)
        node1=node_list.pop()
        node2=node_list.pop()
        merged_node=Node()
        merged_node.freq=node1.freq+node2.freq
        merged_node.l=node1
        merged_node.r=node2
        node_list.append(merged_node)
    return merged_node
encode_dict={}
decode_dict={}


"""Assign a bit symbol 0 to the left branch, assign a bit symbol 1 to the right branch
    The traversal is achieved by using in-order method"""
def label(head,code):
    global encode_dict, decode_dict
    if head:
        label(head.l,code+'0')
        head.code=code
        if head.name:# leave character
            encode_dict[head.name]=head.code
            decode_dict[head.code]=head.name
        label(head.r,code+'1')

def get_dict():
    return encode_dict,decode_dict

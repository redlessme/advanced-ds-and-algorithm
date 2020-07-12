# Name: Siyuan Yan
# ID: 28498704
from huffman_code import *
from Boyer_Moore import *
import sys
from bitarray import bitarray

"""convert string into 8-bits ascii"""
def to_ascii(_string):
    """
    :param _string: a character
    :return: a 8 bits ascii
    """
    res=''
    for char in _string:
        bits=bin(ord(char))[2:]
        bits='0'*(8-len(bits))+bits
        res+=bits
    return res
"""generate the number's elias code like L3L2L1N"""
def elias(num):
    """
    :param num
    :return: elias code
    """
    N=bin(num)[2:]
    L=len(N)
    L-=1

    while L>1:
        bin_L=bin(L)[2:]
        bin_L='0'+bin_L[1:]
        N = bin_L + N
        L=len(bin_L)-1
    if L==1:
        N='0'+N
    return N
"""construct header"""
def generate_header(text):
    if len(text)==0:
        return ""
    header = ''
    uni_list = []
    for char in text:
        if char not in uni_list:
            uni_list.append(char)
    uni_char_num = len(uni_list)
    uni_char_num = elias(uni_char_num)
    header += uni_char_num
    ##sort
    uni_list = sorted(uni_list)

    for char in uni_list:
        ascii_char = to_ascii(char)
        header += ascii_char
        huff_code = encode_dict[char]
        len_huff = len(huff_code)
        len_huff = elias(len_huff)
        header += len_huff
        header += huff_code
    return header
"""lzss to generate the data part, I also use the BoyerMoore Algorithm to find the matched substring  """
def lzss(text,w,l):
    # """construct data part"""
    if len(text) == 0:
        return ""
    i = 0
    res = []
    data=''
    while i < len(text):
        buf = text[i:i + l]
        if i - w < 0:
            dict = text[0:i]
        else:
            dict = text[i - 6:i]
        window = dict + buf
        if buf[0] not in dict:
            format = (1, buf[0])
            res.append(format)
            i += 1
            continue
        else:
            matched = ''
            length = 0
            offset = 0
            for j in range(len(buf)):
                matched += buf[j]
                index_list = BM(window, matched)
                # print("indedx_list",index_list)
                index_list1 = []
                for index in index_list:
                    if index < len(dict):
                        index_list1.append(index)
                if len(index_list1) == 0:
                    break
                length += 1
                offset = len(dict) - max(index_list1)
            if length < 3:
                format = (1, buf[0])
                i += 1
            else:
                format = (0, offset, length)
                i += length
            res.append(format)
    total_number=elias(len(res))
    data+=total_number
    for tuple in res:
        data+=str(tuple[0])
        if tuple[0]==1:
            data+=encode_dict[tuple[1]]
        if tuple[0]==0:
            data+=elias(tuple[1])
            data+=elias((tuple[2]))
    return data

if __name__ == '__main__':

    name=sys.argv[1]
    w=sys.argv[2]
    l=sys.argv[3]
    w=int(w)
    l=int(l)
    f=open(name,'r')
    text=f.read()
    dict = calculate_Frequency(text)
    tree = buildHuffmanTree(dict)
    if len(dict)>1:
        label(tree,'')
    encode_dict,decode_dict=get_dict()
    head=generate_header(text)
    data = lzss(text,w,l)
    result=head+data
    result=bitarray(result)
    f=open("output_lzss_encoder.bin","wb")
    result.tofile(f)
    f.close()
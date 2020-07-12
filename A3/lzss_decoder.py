# Name: Siyuan Yan
# ID: 28498704
import sys
from bitarray import bitarray
def decode(header):
    """start to decode header"""
    res=''
    i=0
    #decode number of unique number
    encoder_dict={}
    decoder_dict={}
    move,unique_num= elias_val(header,i)
    i += move #i=3
    # print("m",move)
    for _ in range(unique_num):
        ascii_code=header[i:i+8]
        char=chr(int(ascii_code,2)) #a

        i+=8
        i,next_read=elias_val(header,i)
        huff_code=header[i:i+next_read]
        i+=next_read
        encoder_dict[char]=huff_code
        decoder_dict[huff_code]=char

    """ start decode data part"""
    i,total_field_num=elias_val(header,i)
    for _ in range(total_field_num):
        if header[i]=='1':
            i+=1
            find_huff=header[i]
            count=1

            while find_huff not in decoder_dict:
                count+=1
                find_huff=header[i:i+count]
            res+=decoder_dict[find_huff]
            i+=len(find_huff)
        elif header[i]=='0':
            i+=1
            i,offset=elias_val(header,i)
            i,mathed_length=elias_val(header,i)
            read_pos=len(res)-offset
            pt1=read_pos
            for _ in range(mathed_length):
                res+=res[pt1]
                pt1+=1
    return res


"""decode the elias codes to original value"""
def elias_val(bin_num,cur):
    L=1
    while True:
        if bin_num[cur]== '0':
            bin_num= bin_num[:cur] + '1' + bin_num[cur + 1:]
            bi_num= bin_num[cur:cur + L]
            L=int(bi_num,2)
            cur+=len(bi_num)
            L+=1
        if bin_num[cur]=='1':
            res=bin_num[cur:cur+L]
            cur+=L
            break
    next_read=int(res,2)
    return cur,next_read

if __name__ == '__main__':


    text = sys.argv[1]
    txt = bitarray()
    f1 = open(text, "rb")
    txt.fromfile(f1)
    f1.close()
    txt = txt.to01()

    result = decode(txt)
    f2=open("output_lzss_decoder.txt",'w')
    f2.write(result)
    f2.close()


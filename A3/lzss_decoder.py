import sys


def decoder(bits):
    k = 1
    z = 0
    value = bits[z:z + k]
    while value[0] == '0':
        value = '1' + value[1::]
        _next = z+k
        z = _next
        k = int(value, 2) + 1
        _next = z+k
        value = bits[z: _next]
    return int(value,2), _next


inputFile = sys.argv[1]

with open(inputFile, 'r') as myfile:
    bits=myfile.read().replace('\n', '')


W = sys.argv[2]
L = sys.argv[3]

W = int(W)
L = int(L)

#bits = '10110000110110000110110001100110001001011000100011011101100001'



curr = 0
final = []

while curr < len(bits):
    if bits[curr]=='0':
        offset, next1 = decoder(bits[curr+1::])
        length, next2 = decoder(bits[curr+1+next1::])
        temp = (0,offset,length)
        final += [temp]
        curr+=next1+next2+1
    elif bits[curr]=='1':
        char = chr(int(bits[curr+1:curr+9], 2))
        temp = (1,char)
        final += [temp]
        curr+=9


string = ''
for i in range(len(final)):
    tup = final[i]
    if tup[0] == 1:
        string+=tup[1]
    elif tup[0] == 0:
        offset = tup[1]
        length = tup[2]
        double = string[len(string)-offset::]*2
        string += double[0:length]

#print(string)
file = open('output_lzss_decoder.txt', 'w')
file.write(string)
file.close()
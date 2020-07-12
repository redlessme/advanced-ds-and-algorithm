#
# def calculateZ(aString):
#     Z=[0]*len(aString)
#     left,right=0,0
#     for k in  range (1,len(aString)):
#         if k>right: #case 1
#             left=right=k
#             #until first mismatch
#             while(right<len(aString) and aString[right]==aString[right-left]):
#                 right+=1
#             Z[k]=right-left
#             right=right-1
#         else:#case2
#             k1=k-left
#             if Z[k1]<right-k+1:#case 2a: Z_k box is inside the Z_l box
#                 Z[k]=Z[k1]
#             else:#case2b
#                 left=k
#                 while(right<len(aString) and aString[right]==aString[right-left]):
#                     right+=1
#                 Z[k]=right-k
#                 right-=1
#     return Z
#
#
# def mathPattern(pattern, string):
#     newString= pattern + "$" + string
#     Z=calculateZ(newString)
#     print(Z)
#     res=[]
#
#     for i in  range(len(Z)):
#         if Z[i]==len(pattern):
#             res.append(i-len(pattern)-1)
#
#     return res
# # if __name__ == '__main__':
# #     text="aabxcaabxaabxay" #15
# #     pattern="aabx"#4
# #
# #     res=mathPattern(pattern,text)
# #     # for i in res:
# #     #     print(text[i:i+len(pattern)])
# #
# #
# # # 0 5 9
#
# if __name__ == '__main__':
#     f = open("reference.txt","r")
#     txt = f.readline()
#
#     f.close()
#     f1=open("pattern-collection.txt","r")
#     for pat in f1.readlines():
#         print(mathPattern(pat.strip(),txt))
#
#
#
#

def calculateZ(aString):
    Z=[0]*len(aString)
    left,right=0,0
    for k in  range (1,len(aString)):
        if k>right: #case 1
            left=right=k
            #until first mismatch
            while(right<len(aString) and aString[right]==aString[right-left]):
                right+=1
            Z[k]=right-left
            right=right-1
        else:#case2
            k1=k-left
            if Z[k1]<right-k+1:#case 2a: Z_k box is inside the Z_l box
                Z[k]=Z[k1]
            else:#case2b
                left=k
                while(right<len(aString) and aString[right]==aString[right-left]):
                    right+=1
                Z[k]=right-k
                right-=1
    return Z
def mathPattern(pattern, string):
    newString= pattern + "$" + string
    Z=calculateZ(newString)
    res=[]

    for i in  range(len(Z)):
        if Z[i]==len(pattern):
            res.append(i-len(pattern))

    return res
# if __name__ == '__main__':
#     text="aabxcaabxaabxay" #15
#     pattern="aabx"#4
#
#     res=mathPattern(pattern,text)
#     for i in res:
#         print(text[i:i+len(pattern)])
#
#
# # 0 5 9
if __name__ == '__main__':
    f = open("reference.txt","r")
    txt = f.readline()

    f.close()
    f1=open("pattern-collection.txt","r")
    for pat in f1.readlines():
        print(mathPattern(pat.strip(),txt))







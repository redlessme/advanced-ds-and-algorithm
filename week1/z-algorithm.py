
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
    print(Z)
    for i in  range(len(Z)):
        if Z[i]==len(pattern):
            res.append(i-len(pattern)-1)

    return res

def sol(string):
    z=calculateZ(string)
    p=0
    print(z)
    for i in range(len(string)):
        if z[i]+i==len(string):
            p=i
            j=p+i
            repeated=True
            while j<len(string):
                if z[j]+j==len(string):
                    j+=p
                    if j > len(string):
                        repeated=False
                        break
                    continue
                repeated=False
                break
            if repeated:
                print(p)
            else:
                print("not periodic")
            break

if __name__ == '__main__':
    txt='abcdabcdabcd'
    sol(txt)


    # text="aabxcaabxaabxay" #15
    # pattern="aabx"#4

    # pattern='defabc'
    # text='abcdfabcdf'
    # res=mathPattern(pattern,text)
    # for i in res:
    #     print(text[i:i+len(pattern)])


# # 0 5 9
# if __name__ == '__main__':
#     f = open("reference.txt","r")
#     txt = f.readline()
#
#     f.close()
#     f1=open("pattern-collection.txt","r")
#     for pat in f1.readlines():
#         print(mathPattern(pat.strip(),txt))







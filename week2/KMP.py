from z import calculateZ



def computeSP(pat):
    m=len(pat)
    z=calculateZ(pat)
    SP=[ 0 for _ in range(m)]
    for j in range(m-1,-1,-1):
        i=j+z[j]-1
        if i==-1:
            break
        SP[i]=z[j]
    return SP


def KMP(txt,pat):
    n=len(txt)
    m=len(pat)
    sp=computeSP(pat)
    j=0
    target=[]
    while j<=n-m:
        i=0
        while i<m and pat[i]==txt[j+i]:
            i+=1
        k=i #missmatched or fully
        if k==m: #fully matched
            # print("Substring at {}".format(j))
            target.append(j)
            shift=m-sp[m-1]
        elif k>0:
            shift=k-sp[k-1]
        else:# no matched
            shift=1
        j+=shift
    return target



# txt1='TTATTTATTTATA'
# pat ='TTATTTAT'
# print(txt1)
# print(KMP(txt1, pat))
# print(computeSP(pat))

txt1 = 'TTATTTATTTATA'
pat = 'TTATTTAT'
print(KMP(txt1,pat))

# print(mathPattern(pat, txt1))
# txt="CCBCCQWEQWEQ"
# pat="CCQWE"
# txt="abcxabcdabxabcdabcdabcy"
# pat="abcdabcy"
#
# print(KMP(txt,pat))

# if __name__ == '__main__':
#     a=[]#kmp
#     b=[]#z
#     f = open("reference.txt","r")
#     txt = f.readline()
#
#     f.close()
#     f1=open("pattern-collection.txt","r")
#     for pat in f1.readlines():
#         a.append(KMP(txt,pat.strip()))
#         b.append(mathPattern(pat.strip(), txt))
#     print(a==b)
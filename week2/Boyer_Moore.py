from z import calculateZ
import copy


# x='ABCDABC'
def jumptable(pat):
    m=len(pat)
    R=[[-1 for _ in range(26)] for _ in range(m)]
    for i in range(1,m):
        R[i]=copy.deepcopy(R[i-1])
        R[i][ord(pat[i-1])-ord('A')]=i-1
    return R

def goodsufix(pat):
    m=len(pat)
    z=list(reversed(calculateZ(pat[::-1])))
    good_suffix=[-1 for _ in range(m+1)]
    for p in range(m):
        j=m-z[p]
        good_suffix[j]=p
    good_suffix.pop()
    return good_suffix

def matchedprefix(pat):
    m=len(pat)
    matched_prefix=[-1 for _ in range(m)]
    z=calculateZ(pat)
    for i in range(m-1,-1,-1):
        if i+z[i]-1==m-1:
            matched_prefix[i]=z[i]
        elif i==m-1:# 最后一位且不匹配
            matched_prefix[i]=0
        else:
            matched_prefix[i]=matched_prefix[i+1]
    matched_prefix[0]=m-1
    return matched_prefix
print(matchedprefix('ABB'))

def BM(txt,pat):
    m=len(pat)
    n=len(txt)
    R=jumptable(pat)
    good_suffix=goodsufix(pat)
    matched_prefix=matchedprefix(pat)
    i=0
    target=[]
    while i<=n-m:
        j=m-1
        while j>=0 and pat[j]==txt[i+j]:
            j-=1
        k=j #missmatched or fully macthed index
        if k==-1: #fully matched  #good  rule case  2
            n_goodsufix=m-matched_prefix[1]
            n_bad=0
            # print ("Substring found at index {} using Boyer Moore algorithm".format(i))
            target.append(i)
        elif k==m-1: # bad case no macthed good suffix
            n_goodsufix=0
            r=R[k][ord(txt[i+k])-ord('A')]
            n_bad=max(1,k-r)
        else: # compare bad and good rule
            #bad rule
            r=R[k][ord(txt[i+k])-ord('A')]
            n_bad=max(1,k-r)
            #good rule
            if good_suffix[k+1]>0:#case 1a
                n_goodsufix=m-good_suffix[k+1]-1
            else: #case 1b
                n_goodsufix=m-matched_prefix[k+1]
        shift=max(n_goodsufix,n_bad)
        i+=shift


    return target
txt='TTATTTATATTTAT'
worng_pat='TTATTTAT'
# print(txt)
print(BM(txt,worng_pat))

# BM("CCBCCQWEQWEQ","CCQWE")
# BM("AACCCCBDC","CCCC")
#
#
#
# txt="CCBCCQWEQWEQ"
# pat="CCQWE"
# txt="abcxabcdabxabcdabcdabcy"
# pat="abcdabcy"



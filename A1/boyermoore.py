# Name: Siyuan Yan
# ID: 28498704
import copy
CHARACTER = 75
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
def jumptable(pat):
    m=len(pat)
    R=[[-1 for _ in range(CHARACTER)] for _ in range(m)]
    for i in range(1,m):
        R[i]=copy.deepcopy(R[i-1])
        R[i][ord(pat[i-1])-ord('0')]=i-1
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
    print(z)
    for i in range(m-1,-1,-1):
        if i+z[i]-1==m-1:
            matched_prefix[i]=z[i]
        elif i==m-1:# last position and missmatched
            matched_prefix[i]=0
        else:
            matched_prefix[i]=matched_prefix[i+1]
    matched_prefix[0]=m-1
    return matched_prefix

print(matchedprefix("abababab"))

def BM(txt,pat):
    m=len(pat)
    n=len(txt)
    R=jumptable(pat)
    good_suffix=goodsufix(pat)
    matched_prefix=matchedprefix(pat)
    i=0
    target=[]
    skip_point = -20
    while i<=n-m:
        j = m - 1
        good_case1a = False
        galil=False
        while j>=0 and pat[j]==txt[i+j]:
            if i+j==skip_point: #match
                galil=True      #gali optimisation applied
                break
            j-=1
        k=j #missmatched or fully macthed index
        if k==-1 or galil==True: #fully matched  #good  rule case  2
            if m!=1:# make sure that do not out of index when length of pat is 1
                n_goodsufix=m-matched_prefix[1]
            else:
                n_goodsufix = m
            n_bad = 0
            target.append(i + 1)
        elif k==m-1: # bad case no macthed good suffix
            n_goodsufix=0
            r=R[k][ord(txt[i+k])-ord('0')]
            n_bad=k-r
        else: # compare bad and good rule
            #bad rule
            r=R[k][ord(txt[i+k])-ord('0')]
            n_bad=max(1,k-r)
            #good rule
            if good_suffix[k+1]>0:#case 1a
                n_goodsufix=m-good_suffix[k+1]-1
                good_case1a=True
            else: #case 1b
                n_goodsufix=m-matched_prefix[k+1]
        shift=max(n_goodsufix,n_bad)
        if shift==n_goodsufix and good_case1a==False:# good case 1b or 2, skipoint is used to check galil optimisation
            skip_point=i+m-1
        else:# other case ,  dont use galil rule in next iteration
            skip_point=-20
        i+=shift
    return target

# Name: Siyuan Yan
# ID: 28498704
import sys
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

def computeSPx(pat):
    m=len(pat)
    z=calculateZ(pat)
    #The size of Spi is m*75, each sublist records the length of the longest proper suffix of pat[1...i] that matches its prefix, with the extra condition
    # that pat[spi(x)+1]=x
    SP=[ [0 for _ in range(CHARACTER)] for _ in range(m)]
    for j in range(m-1,-1,-1):
        #for each j,compute its i will record spi with the longest when multiple z_box with different start point j but same end point i
        i=j+z[j]-1
        if i==-1:# if i=-1 sp[i] will be recognised as the last value of SP
            break
        SP[i][ord(pat[z[j]])-ord('0')]=z[j]#recording spi and the next character
    return SP
def KMP(txt,pat):
    n=len(txt)
    m=len(pat)
    sp=computeSPx(pat)
    j=0
    target=[]
    ignore=0 #we dont need compare the sp part in next iteration
    while j<=n-m:
        i=ignore
        while i<m and pat[i]==txt[j+i]:
            i+=1
        k=i #missmatched or fully
        if k==m: #fully matched
            target.append(j)
            if j+m!=n:# make sure that do not out of index when length of pat is 1
                #find the sp of pat that next character of prefix is mismatched x in txt
                shift=m-sp[m-1][ord(txt[j+m])-ord('0')]
                ignore=sp[m-1][ord(txt[j+m])-ord('0')]
            else:# finsh all comparison, break
                j=n
                shift=0
        elif k>0:#general case
            shift=k-sp[k-1][ord(txt[j+k])-ord('0')]
            ignore=sp[k-1][ord(txt[j+k])-ord('0')]
        else:# no matched
            shift=1
            ignore=0
        j+=shift
    return target

if __name__ == '__main__':
    t=sys.argv[1]
    p=sys.argv[2]
    f = open(t,"r")
    txt = f.read()
    txt = txt.strip()
    f.close()
    f1=open(p,"r")
    pat=f1.read()
    pat=pat.strip()
    f1.close()
    output=open("output_kmp.txt",'w')
    kmp=KMP(txt,pat)
    for pos in kmp:
        output.write(str(pos)+'\n')
    output.close()

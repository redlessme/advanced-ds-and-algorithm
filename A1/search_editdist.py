# Name: Siyuan Yan
# ID: 28498704
import sys
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
def edit_distance(text,pat):
    str=pat+"$"+text
    z1=calculateZ(str)
    reverse_str=pat[::-1]+"$"+text[::-1]
    z2=calculateZ(reverse_str)
    str_len=len(str)
    m=len(pat)
    target=[]
    if m==1:
        for i in range(m+1,len(z1)):
            if z1[i]==m: #match
                target.append([i-m,0])
            else:    #substitution
                target.append([i-m,1])
    else:
        for i in range(m+1,str_len-m+2):
            # sum the z value of the first character and the z value of the last character in current pattern
            substitution=z1[i]+z2[str_len-i+1]
            #sum the z value of the first character and the z value of  the next character of the last character in current pattern
            deletion=z1[i]+z2[str_len-i]
            # sum the z value of the first character and the z value of the character that before the last character in current pattern
            insertion=z1[i]+z2[str_len-i+2]
            if z1[i]==m:
                target.append([i-m,0])
            # the extra case 'i<=str_len-m 'make sure if the length of remain text < the length of pattern, then it should not use substitution
            elif substitution==m-1 and i<=str_len-m:
                target.append([i-m,1])
            elif insertion==m-1 and i<=str_len-m+1:
                target.append([i-m,1])
            elif deletion==m and i<=str_len-m-1:
                if z1[i+1]!=m:# if the pattern that start from i+1 matches the pat,ignore the case that start from i as redundant
                    target.append([i-m,1])
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
    output=open("output_editdist.txt",'w')
    ed=edit_distance(txt,pat)
    for ele1,ele2 in ed:
        output.write(str(ele1)+' '+str(ele2)+'\n')
    output.close()




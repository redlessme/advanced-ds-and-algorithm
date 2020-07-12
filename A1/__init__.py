from z import calculateZ
import sys
def edit_distance(text,pat):
    str=pat+"$"+text
    z1=calculateZ(str)
    reverse_str=pat[::-1]+"$"+text[::-1]
    z2=calculateZ(reverse_str)
    str_len=len(str)
    m=len(pat)
    target=[]
    for i in range(m+1,str_len-m+2):
        if str_len - i + 2 <= str_len - 1:
            # sum the z value of the first character and the z value of the last character in current pattern
            substitution=z1[i]+z2[str_len-i+1]
            #sum the z value of the first character and the z value of  the next character of the last character in current pattern
            deletion=z1[i]+z2[str_len-i]
            # sum the z value of the first character and the z value of the character that before the last character in current pattern
            # if str_len-i+2<=str_len-1:
            insertion=z1[i]+z2[str_len-i+2]
        else:
            continue

        if z1[i]==m:
            print(str[i:i + 5])
            print("match", i)
            target.append([i-m,0])
        # the extra case 'i<=str_len-m 'make sure if the length of remain text < the length of pattern, then it should not use substitution
        elif substitution==m-1 and i<=str_len-m:
            print(str[i:i + 5])
            print("sub",i,substitution)
            target.append([i-m,1])
        elif insertion==m-1 and i<=str_len-m+1:
            print(str[i:i + 5])
            print("insert",i,insertion)
            target.append([i-m,1])
        elif deletion==m and i<=str_len-m-1:
            print(str[i:i + 5])
            if z1[i+1]!=m:# if the pattern that start from i+1 matches the pat,ignore the case that start from i as redundant
                print("delete",i,deletion)
                target.append([i-m,1])
    return target

if __name__ == '__main__':
    # text = "abcdadcbadcba"
    # print(len(text))
    # pattern = "a"
    # res=edit_distance(text,pattern)
    # print(res)
    text='abdyabxcdyabcdz'
    pat='abcd'
    res=edit_distance(text,pat)
    print(res)


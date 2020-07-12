import sys
from z import calculateZ
def search_editdist_zalg(text, pat):
    pat_len = len(pat)
    txt_len = len(text)
    first_string = pat + "$" + text
    # create the first string by concatenating pattern, "$", and text
    str_len = len(first_string)
    first_lis = calculateZ(first_string)
    # calculate the z values for the first string
    second_string = pat[::-1] + "$" + text[::-1]
    # create the second string by concatenating reversed pattern, "$", and reversed text
    second_lis = calculateZ(second_string)
    # calculate the z values for the second string
    result = []
    for i in range(pat_len + 1, str_len - pat_len + 2):
        substitute_sum = first_lis[i] + second_lis[txt_len+pat_len+2-i]
        # sum the z value of the first character of the pattern in the first string, and the z value of the
        # last character in the second string. Case substitution
        delete_sum = first_lis[i] + second_lis[txt_len+pat_len+2-i-1]
        # sum the z value of the first character of the pattern in the first string, and the z value of the
        # one before the last character in the second string so that the corresponding substring with length
        # of len(pat) + 1. Case insertion
        insert_sum = first_lis[i] + second_lis[txt_len+pat_len+2-i+1]


        # sum the z value of the first character of the pattern in the first string, and the z value of the
        # second last character in the second string so that the corresponding substring with length
        # of len(pat) - 1. Case deletion
        if substitute_sum == pat_len*2:
            print("match", i, substitute_sum)
            print(first_string[i:i + 5])
            result.append([i - len(pat), 0])
            # if they exactly match
        elif substitute_sum == pat_len-1:
            print("sub", i, substitute_sum)
            print(first_string[i:i + 5])
            result.append([i - len(pat), 1])
            # if they match with hamming distance = 1
        elif insert_sum== pat_len-1:
            print("insert",i,insert_sum)
            print(first_string[i:i+5])
            result.append([i - len(pat), 1])
            # if they match by deleting one character from pattern
        elif delete_sum == pat_len:
            # if they match by inserting one character into pattern
            if first_lis[i+1] + second_lis[txt_len+pat_len+1-i] != 2*pat_len:#删除的时候，防止下一位开始正好完全匹配
                print("delete", i, delete_sum)
                print(first_string[i:i + 5])
                result.append([i - len(pat), 1])
        # 1. This conditional statement will check cases in order, if any cases matched, it will not consider
        # the other cases. For example, if xyz matches xyz, then xy matches xyz with edit distance = 1 will
        # not be included
        # 2. When insertion case happens at i, the position will be stored only if there is not any exactly match at
        # i+1
        # 3. When there is an exactly match at i, the deletion case at i+1 will not be considered because
        # its corresponding z_value in the second string will be the length of the pattern, exceeding the len -1
    return result


# print(search_editdist_zalg("abdyabxdcyabcdz", "abcd"))

if __name__ == "__main__":
    # text='abdyabxcdyabcdz'
    # pat='abcd'
    # res=search_editdist_zalg(text,pat)
    # print(res)
    # txt='abdyabxdcyababcd'
    # pat='abcd'
    # search_editdist_zalg(txt,pat)
    # txt = "abdabxdabxcdabcdz"
    # pat = "abcd"
    # search_editdist_zalg(txt, pat)
    # text = "abcdadcbadcba"
    # pattern = "a"
    # search_editdist_zalg(text,pattern)
    text = 'abdyabxcdyabcdz'
    pat = 'abcd'
    res = search_editdist_zalg(text, pat)
    print(res)
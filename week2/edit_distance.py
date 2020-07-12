def edit_distance(word1,word2):
    s1=len(word1)+1
    s2=len(word2)+1
    matrix=[[0 for _ in range(s2)]for _ in range(s1) ]  #s1 *s2 matrix

    for i in range(s2):
        matrix[0][i]=i
    for j in range(s1):
        matrix[j][0]=j

    print(matrix)

    for i in range(1,s1):
        for j in range(1,s2):
            if word1[i-1]==word2[j-1]:
                matrix[i][j]=matrix[i-1][j-1]
            else:
                matrix[i][j]=min(1+matrix[i-1][j-1],1+matrix[i-1][j],1+matrix[i][j-1])
    return matrix[s1-1][s2-1]
if __name__ == '__main__':
    print(edit_distance("bird","birs"))



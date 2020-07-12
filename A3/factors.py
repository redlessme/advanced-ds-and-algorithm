# Name: Siyuan Yan
# ID: 28498704
import random
import sys

def factorize(n):
    a = []
    res=''
    count=0
    while n % 2 == 0:
        a.append(2)
        n /= 2
        count+=1
    res+='2^'
    res+=str(count)
    f = 3
    count=0
    flag=False
    while f * f <= n:
        if n % f == 0:
            flag = True
            a.append(f)
            count+=1
            n /= f

        else:
            f += 2
    if flag==True:
        res+=' x 3^'+str(count)

    if n != 1:
        a.append(int(n))
        res+=' x '+str(int(n))+'^1'

    return res

def Primary_Test(n,k):
    if n<2 or n==4:
        return False
    if n==2 or n==3:
        return True
    if n % 2 == 0:
        return False
    t=n-1
    s=0
    while(n%2==0):
        s+=1
        t=t//2
    for j in range(k):
        a=random.randint(2,n-2)
        if pow(a,n-1,n)!=1:
            return False
    return True

if __name__ == '__main__':
    #N=input("input a number N:")
    N = sys.argv[1]
    N=int(N)
    if N<547:
        print("N should be greater or equal to 547")
    else:
        C=[]
        i=N
        count=0
        for i in range(N-1,1,-1):
            if Primary_Test(i,100):
                C.append(i+1)
                count+=1
            if count==100:
                break

        C=C[::-1]


        fp=open("output_factors.txt",'w')
        for c in C:
            fp.write(str(c).rjust(3)+' '+factorize(c)+'\n')



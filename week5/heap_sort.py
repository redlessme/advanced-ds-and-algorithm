# def MaxHeapify(array,n,i):
#     l = 2*i+1
#     r = 2*i+2
#     largest = i
#     if l<=n and array[l]>array[largest]:
#         largest = l
#     if r<=n and array[r]>array[largest]:
#         largest = r
#     if largest != i:
#         array[largest],array[i] = array[i],array[largest]
#         MaxHeapify(array,n,largest)

def MaxHeapify(array,n,i):

    while 2*i<=n:
        l = 2 * i
        r = 2 * i + 1
        largest = l
        if l<n and array[r]>array[l]:
            largest=r
        if array[largest]>array[i]:
            array[i],array[largest]=array[largest],array[i]
            i=largest
        else:
            break

def HeapSort(array):
    n = len(array)
    for i in reversed(range(n//2)):
        MaxHeapify(array,n-1,i)
    while n>1:
        array[n-1],array[0] = array[0],array[n-1]
        n -= 1
        MaxHeapify(array,n-1,0)
    return array

if __name__ == '__main__':
    alist=[1,2,5,3,9,23,-3,-3,4,90,3,6,-2]
    print(HeapSort(alist))
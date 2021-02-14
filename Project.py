import BinarySearch

def sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        sort(L)
        sort(R)
        join(arr,L,R)
        print('Intermediate Steps: ',arr)

def join(arr,L1,L2):

    n1 = len(L1)
    n2 = len(L2)

    i = 0
    j = 0
    k = 0

    while i<n1 and j<n2:
        if L1[i] <= L2[j]:
            arr[k] = L1[i]
            i += 1
        else:
            arr[k] = L2[j]
            j += 1

        k += 1

    while i<n1:
        arr[k] = L1[i]
        i += 1
        k += 1
    while j<n2:
        arr[k] = L2[j]
        j += 1
        k += 1


n = int(input('Enter no of values(n) to sort: '))
print('Enter values: ',end=' ')
arr = list(map(int,input().split()))[0:n]
print('unsorted array: ',arr)

sort(arr)
print('sorted array: ',arr)

print('Enter the element you want to search in sorted arr {}: '.format(arr),end=' ')
key = int(input())
if BinarySearch.Bsearch(arr,key):
    print('Element is Found')
else:
    print('Element is not Found')
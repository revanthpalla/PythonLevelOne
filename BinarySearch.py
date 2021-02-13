def Bsearch(arr,key,l,r):
    if l<=r:
        mid = l+(r-1)//2
        if arr[mid] == key:
            return True
        elif arr[mid]<key:
            l = mid+1
            return Bsearch(arr,key,l,r)
        else:
            r = mid-1
            return Bsearch(arr,key,l,r)
    else:
        return False

#Testing
arr = [10,20,30,40,50,60]
if Bsearch(arr,50,0,len(arr)):
    print('Element is Found')
else:
    print('Element not Found')

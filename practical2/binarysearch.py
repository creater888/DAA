def BinarySearch(arr,n,key):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[4,56,56,67,78,87,679,89866]
n=len(arr)
key=87
ans=BinarySearch(arr,n,key)
print(ans)
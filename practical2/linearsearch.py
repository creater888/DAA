def linearSearch(arr,n,key):
    for i in range(n):
        if arr[i]==key:
            return i
    return -1

arr= [12,23,45,54,76]
n=len(arr)
key =54
ans=linearSearch(arr,n,key)
print(ans)


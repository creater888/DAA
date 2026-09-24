def Insertionsort(arr,n):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

arr=[78,67,87,56,679,89866,56,4]
n=len(arr)
a=Insertionsort(arr,n)
print(a)
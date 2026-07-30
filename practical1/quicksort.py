def Partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[i+1]
    arr[i+1]=arr[high]
    arr[high]=temp
    return i+1

def Quicksort(arr,low,high):
    if low<high:
        pi=Partition(arr,low,high)
        Quicksort(arr,low,pi-1)
        Quicksort(arr,pi+1,high)
    return arr

arr=[78,67,87,56,679,89866,56,4]
n=len(arr)
a=Quicksort(arr,0,n-1)
print(a)
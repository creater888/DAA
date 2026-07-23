def Selectionsort(arr,n):
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp
    return arr

arr=[78,67,87,56,679,89866,56,4]
n=len(arr)
a=Selectionsort(arr,n)
print(a)
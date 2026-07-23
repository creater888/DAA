def Bubblesort(arr,n):
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
arr =[78,67,87,56,679,89866,56,4]
n=len(arr)
a=Bubblesort(arr,n)
print(a)
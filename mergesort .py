def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        #print(arr[mid])
        lefthalf=arr[:mid]
        righthalf=arr[mid:]
        #print(lefthalf,righthalf)
        mergesort(lefthalf)
        mergesort(righthalf)
        i=j=k=0
        while i<len(lefthalf) and j<len(lefthalf):
            if lefthalf[i]<righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
                k=k+1
            else:
                arr[k]=righthalf[j]
                j=j+1
                k=k+1
        
        while i<len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1

arr=[5,11,2,178,3,111]
mergesort(arr)
print(arr)
def recursiveBubbleSort(array,end=None):
    if end==None:
        end = len(array)
    if end<=1:
        return
    for i in range(0,end-1):
        if array[i]>array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
    recursiveBubbleSort(array,end-1)
    return array
print(recursiveBubbleSort([4,1,5,2,3]))
def recursiveInsertionSort(array,start=1):
    if start==len(array):
        return
    key = array[start]
    j = start-1
    while j>=0 and array[j]>key:
        array[j+1] = array[j]
        j-=1
    array[j+1]=key
    recursiveInsertionSort(array,start+1)
    return array
print(recursiveInsertionSort([5,4,3,2,1]))

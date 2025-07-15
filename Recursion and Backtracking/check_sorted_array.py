def isSorted(array):
    n = len(array)
    if n==0:
        return True
    return array[n-1] >= array[n-2] and isSorted(array[0:n-1])
array1 = [1,9,10,6,7,8,5,20] 
print(isSorted(array1))

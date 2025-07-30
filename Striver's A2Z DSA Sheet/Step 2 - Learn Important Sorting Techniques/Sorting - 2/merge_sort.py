def mergeSort(array):
    # Base Case
    if len(array)==1:
        return array
    mid = len(array)//2

    # Divide
    left_half = mergeSort(array[:mid])
    right_half = mergeSort(array[mid:])

    # Conquer
    return merge(right_half,left_half)
def merge(left,right):
    merged = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
        
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

print(mergeSort([4,1,5,2,3]))
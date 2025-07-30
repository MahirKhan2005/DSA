def quickSort(array):
    if len(array)<=1:
        return array
    pivot = array[len(array)//2]
    left = [x for x in array if x<pivot]
    middle = [x for x in array if x==pivot]
    right = [x for x in array if pivot<x]

    return quickSort(left) + middle + quickSort(right)
print(quickSort([4,1,5,2,3]))

# Best/Avg case TC - O(nlogn)
# Worst case TC - O(n^2) -- when pivot is smallest or largest
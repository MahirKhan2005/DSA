def reverseArray(array,new_array):
    while array:
        element = array.pop()
        new_array.append(element)
    return new_array

print(reverseArray([1,2,3],[]))
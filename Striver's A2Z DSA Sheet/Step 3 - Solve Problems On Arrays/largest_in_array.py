def largestElement(array):
    maximum = array[0]
    for i in range(0,len(array)):
        if array[i]>maximum:
            maximum = array[i]
    return maximum
print(largestElement([5,3,1,4,2]))
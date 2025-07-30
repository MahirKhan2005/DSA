def largestElement(array):
    maximum = array[0]
    for i in range(0,len(array)):
        if array[i]>maximum:
            maximum = array[i]
    return maximum
def smallestElement(array):
    smallest = array[0]
    for i in range(0,len(array)):
        if array[i]<smallest:
            smallest = array[i]
    return smallest
def secondLargestSmallest(array):
    maximum = largestElement(array)
    secondMin = array[0]
    secondlar = array[1]
    minimum = smallestElement(array)
    for i in range(0,len(array)):
        if array[i]<secondMin and array[i]!=minimum:
            secondMin = array[i]
        if array[i]>secondlar and array[i]!=maximum:
            secondlar = array[i]
    print(f"Second smallest - {secondMin}")
    print(f"Second largest - {secondlar}")
    return
secondLargestSmallest([9,8,7,1,2,3,4,5,6,1,4])
print(smallestElement([9,8,7,1,2,3,4,5,6,1,4]))
print(largestElement([9,8,7,1,2,3,4,5,6,1,4]))
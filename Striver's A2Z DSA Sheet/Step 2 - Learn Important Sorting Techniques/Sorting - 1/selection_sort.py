def ss(array):
    for i in range(0,len(array)):
        minimum_index = i
        for j in range(i,len(array)):
            if array[j]<array[minimum_index]:
                minimum_index = j
        temp = array[minimum_index]
        array[minimum_index] = array[i]
        array[i] = temp
    return array
print(ss([4,1,5,2,3]))
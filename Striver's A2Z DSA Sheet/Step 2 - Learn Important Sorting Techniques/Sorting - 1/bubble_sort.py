def bs(array):
    for i in range(0,len(array)-1):
        swaped = False
        for j in range(1,len(array)-i):
            if array[j]<array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                swaped = True
        if swaped==False:
            break
    return array
print(bs([4,1,5,2,3]))
            

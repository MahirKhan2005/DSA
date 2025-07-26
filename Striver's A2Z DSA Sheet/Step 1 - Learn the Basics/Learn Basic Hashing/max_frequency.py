arr = [5,1,3,7,9,5,5,7,9,9]
arr.sort()
d = {}
max_key = None
max_value = 0
for num in arr:
    d[num] = d.get(num,0) + 1
    if d[num]>max_value:
        max_key = num
        max_value = d[num]
print(d)
print(f"{max_key} {max_value}")
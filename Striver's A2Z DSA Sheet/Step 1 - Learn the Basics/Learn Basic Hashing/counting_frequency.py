a = [1,2,5,7,3,4,6,3]
d={}
for num in a:
    d[num] = d.get(num,0) + 1
print(d)
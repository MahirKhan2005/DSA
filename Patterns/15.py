def pattern(n):
    if n==0:
        return
    for i in range(0,n):
        print(chr(65+i),end=" ")
    print()
    pattern(n-1)

pattern(5)
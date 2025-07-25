def pattern(n):
    if n==0:
        return
    for i in range(1,n+1):
        print(i,end="")
    print()
    pattern(n-1)

pattern(5)
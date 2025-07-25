def pattern(n):
    for i in range(1,n+1):
        print(i*"*")
    for i in range(0,n-1):
        print((n-i-1)*"*")

pattern(5)

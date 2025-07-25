def pattern(n):
    for i in range(1,n+1):
        print((n-i)*" " + "*"*(2*i - 1))
    for i in range(0,n):
        print((i)*" " + "*"*(2*(n-i) - 1))
pattern(5)
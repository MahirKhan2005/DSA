def pattern(n):
    for i in range(0,n):
        print((i)*" " + "*"*(2*(n-i) - 1))
pattern(5)
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print(2*(n-i)*" ",end="")
        for k in range(1,i+1):
            print(i-k+1,end="")
        print()

pattern(4)
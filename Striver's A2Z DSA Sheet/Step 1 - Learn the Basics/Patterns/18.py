def pattern(n):
    k=n
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(65+k-2+j),end="")
        k-=1
        print()

pattern(5)
def pattern(n):
    for i in range(1,n+1):
        print((n-i)*" ",end="")
        for j in range(1,i+1):
            print(chr(65+j-1),end="")
        if i==1:
            print()
            continue
        for k in range(1,i):
            print(chr(65+i-k-1),end="")
        print()
            
pattern(5)
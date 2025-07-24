def pattern(n):
    for i in range(0,n):
        start = 1 if i%2==0 else 0
        for j in range(0,i+1): 
            print(start,end=" ")
            start = 1-start
        print()

pattern(5)
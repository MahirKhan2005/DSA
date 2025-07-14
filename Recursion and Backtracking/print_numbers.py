def printNums(n):
    if n==1:
        print(1)
        return
    print(f"{n}") 
    printNums(n-1)

printNums(6)
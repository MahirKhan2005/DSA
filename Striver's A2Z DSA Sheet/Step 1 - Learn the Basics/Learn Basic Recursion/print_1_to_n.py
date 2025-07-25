def numbers(i,n):
    if i>n:
        return
    if i<=n: 
        print(i)
    numbers(i+1,n)

numbers(1,5)
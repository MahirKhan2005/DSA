def something(n):
    if n==0:
        return
    print("Hello There")
    something(n-1)

something(5)
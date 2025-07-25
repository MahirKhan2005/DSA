def something(name,n):
    if n==0:
        return
    print(f"Hello {name.title()}")
    something(name,n-1)

something("mahir",5)
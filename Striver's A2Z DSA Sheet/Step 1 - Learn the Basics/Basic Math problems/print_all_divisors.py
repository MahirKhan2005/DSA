def print_divisors(n):
    divisors = []
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    print(divisors)
    return
print_divisors(321)

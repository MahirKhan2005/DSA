def isPrime(n):
    divisors = []
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    if len(divisors)==2:
        return True
    else:
        return False

print(isPrime(3121))

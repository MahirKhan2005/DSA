def hcf(n1,n2):
    for i in range(1,min(n1+1,n2+1)):
        if n1%i==0 and n2%i==0:
            gcd = i
    return gcd

print(hcf(10,20))
def armstrong(n):
    sum = 0
    k = n
    while(k>0):
        remainder = k%10
        sum += remainder**3
        k//=10
    if sum==n:
        return True
    else:
        return False

print(armstrong(371))

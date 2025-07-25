def pattern(n):
    k = n
    j=0
    while(k>0):
        print("*"*k + 2*j*" " + "*"*k)
        k-=1
        j+=1
    for i in range(1,n+1):
        print("*"*i + 2*(n-i)*" " + "*"*i)

pattern(5)
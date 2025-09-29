class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        isPrime = [True]*n
        isPrime[0]=isPrime[1]=0
        i=2
        while i*i<n:
            if isPrime[i]:
                for multiple in range(i*i,n,i):
                    isPrime[multiple] = False
            i+=1
        return sum(isPrime)
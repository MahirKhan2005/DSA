# Brute Force approach
# Time Complexity - O(logn)
def count_digits(n):
    count = 0
    while(n>0):
        count+=1
        n//=10
    return count
print(count_digits(5456))

# Algorithmic approach
# Time Complexity - O(1)
import math
def opt_count_digits(n):
    return int(math.log10(abs(n)) +1)
print(opt_count_digits(50))
class Solution(object):
    def reverse(self,x):
        reverse_number = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while(x>0):
            remainder = x%10
            reverse_number = reverse_number*10 + remainder
            x//=10
        reverse_number = reverse_number*sign
        if reverse_number<-2**31 or reverse_number>(2**(31)-1):
            return 0 
        else:
            return reverse_number


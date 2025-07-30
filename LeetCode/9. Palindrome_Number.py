class Solution(object):
    def reverse(self,x):
        reverse_number = 0
        while(x>0):
            remainder = x%10
            reverse_number = reverse_number*10 + remainder
            x//=10
        if reverse_number<-2**31 or reverse_number>(2**(31)-1):
            return 0 
        else:
            return reverse_number
    def isPalindrome(self, x):
        reverse_number = self.reverse(x)
        if reverse_number == x and x>=0:
            return True
        else:
            return False
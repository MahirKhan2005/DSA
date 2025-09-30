class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend<0)^(divisor<0) else 1
        dividend,divisor = abs(dividend),abs(divisor)
        quotient = 0
        while dividend>=divisor:
            temp = divisor
            multiple = 1
            while dividend>=(temp<<1):
                temp<<=1
                multiple<<=1
            dividend-=temp
            quotient+=multiple
        ans = quotient*sign
        if ans<-2**31:
            return -2**31
        if ans>2**31-1:
            return 2**31-1
        return ans
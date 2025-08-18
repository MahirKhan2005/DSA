# TC - O(n) O(1) for both  better without min max function
class Solution(object):
    def maxProfit(self,prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            profit = price - min_price
            if profit > max_profit: max_profit = profit
            if price < min_price: min_price = price
            
            # This is the exact logic as above and same tc - O(n) but because the min max function creates a call stack in the for loop everytime it runs, its slower than the former
            # max_profit = max(profit,max_profit)
            # min_price = min(price,min_price)
        return max_profit
a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))   
class Solution:
    def profit(self,nums):
        if not nums:
            return 0
        min_price =float('inf')
        max_profit=0
        for price in nums:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
    
se = Solution()
nums=[7,6,4,3,1]
print(se.profit(nums))
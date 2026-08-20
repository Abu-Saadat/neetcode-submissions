class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxxprofit = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                maxxprofit = max(maxxprofit, prices[r]-prices[l])
            else:
                l = r 
            r+=1
        return maxxprofit
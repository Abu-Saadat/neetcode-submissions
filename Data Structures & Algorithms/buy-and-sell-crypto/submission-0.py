class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxxprofit = 0
        minnval = float("inf")
        n = len(prices)
        for i in range(n):
            if prices[i] < minnval:
                minnval = prices[i]
            maxxprofit = max(maxxprofit,prices[i]-minnval)
        return maxxprofit

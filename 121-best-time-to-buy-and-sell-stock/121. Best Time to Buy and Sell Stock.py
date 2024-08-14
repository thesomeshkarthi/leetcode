class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, left, right = 0,0,1

        while(right <= len(prices) - 1):
            if(prices[left] < prices[right]):
                profit = prices[right] - prices[left]
                if (profit > maxProfit):
                    maxProfit = profit
            else:
                left = right
            
            right = right + 1
        
        return maxProfit
        
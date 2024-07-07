#Leetcode 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #to keep track of the previous price
        prev_price = prices[0]

        #record total profit
        total_profit = 0

        #we "greedily cumulate" everyday's profit
        #unless the stock is decreasing (we dont count the decrease)
        for x in prices:
            if x > prev_price:
                total_profit += (x - prev_price)
            prev_price = x

        return total_profit
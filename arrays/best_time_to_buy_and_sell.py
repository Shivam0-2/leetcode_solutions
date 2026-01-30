#Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#Approach: Two pointer
#Time Complexity: O(n)
#Space Complexity: O(1)
def maxProfit(self,prices):
        buy,sell=0,1
        maxp= 0
        while sell < len(prices):
            if prices[buy]<prices[sell]:
                profit = prices[sell]-prices[buy]
                maxp = max(maxp,profit)
            else:
                buy = sell
            sell+=1
        return maxp

        
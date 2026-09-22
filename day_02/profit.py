"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 

a different day in the future to sell that stock.

"""

prices = [7,1,5,3,6,4]

left = 0

right = 1

profit = 0

while(right < len(prices)):

    if prices[right] > prices[left]:

        profit = max(profit,prices[right]-prices[left])

    else:

        left = right

    right += 1

print(profit)            

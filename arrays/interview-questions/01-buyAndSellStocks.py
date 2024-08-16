# Function definition
def findMaxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    # using for loop

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif (prices[i] - min_price) > max_profit:
            max_profit = prices[i] - min_price
    return max_profit 











# Driver code
prices = [7, 1, 5, 3, 6, 4, 15]
# Function calling
profit = findMaxProfit(prices)

print("Maximum profit by selling the stock is", profit)
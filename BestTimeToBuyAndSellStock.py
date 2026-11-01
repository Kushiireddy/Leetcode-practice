#121. Best Time To Buy And Sell Stock
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        # Start from the second day as the first day's price is already stored in min_price
        for i in range(1, len(prices)):
            # Get the price on the current day
            current_price = prices[i]

            # Calculate the profit if we sold today a stock we bought a lower price 
            potential_profit = current_price - min_price

            # Update max_profit if we found a better profit
            if potential_profit > max_profit:
                max_profit = potential_profit

            # Update min_price if today's price is lower
            if current_price < min_price:
                min_price = current_price

        # Return the highest profit found
        # If no profitable transaction exists, return 0
        return max_profit

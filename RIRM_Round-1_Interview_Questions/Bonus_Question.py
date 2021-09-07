class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Max profit and price to buy
        max_profit = 0
        high_buy = 0

        # Reverse the array of prices
        prices = prices[::-1]

        # Check each price to sell at compared to the highest buy price ahead of it
        for price in prices:
            # Update highest buy price in front of price
            if price > high_buy:
                high_buy = price
            # Check if this sale make higher profit than sales later in original array
            if high_buy - price > max_profit:
                max_profit = high_buy - price

        # Return the highest profit achieved
        return max_profit
class Solution:
    def maxProfit(self, prices):

        minimum_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < minimum_price:
                minimum_price = price

            profit = price - minimum_price

            if profit > max_profit:
                max_profit = profit

        return max_profit

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)
        answer = right

        while left <= right:

            mid = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:

                answer = mid
                right = mid - 1

            else:

                left = mid + 1

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
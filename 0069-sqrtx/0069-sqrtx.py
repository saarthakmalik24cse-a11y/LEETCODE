class Solution:
    def mySqrt(self, x):

        if x < 2:
            return x

        left = 1
        right = x
        answer = 0

        while left <= right:

            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                answer = mid
                left = mid + 1

            else:
                right = mid - 1

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
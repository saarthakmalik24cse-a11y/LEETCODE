class Solution:
    def containsDuplicate(self, nums):

        seen = {}

        for num in nums:

            if num in seen:
                return True

            seen[num] = 1

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
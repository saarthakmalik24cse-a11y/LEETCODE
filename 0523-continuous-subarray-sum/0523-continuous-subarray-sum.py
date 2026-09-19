class Solution:
    def checkSubarraySum(self, nums, k):

        first = {0: -1}

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            remainder = prefix % k

            if remainder in first:

                if i - first[remainder] >= 2:
                    return True

            else:
                first[remainder] = i

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
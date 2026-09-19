class Solution:
    def subarraySum(self, nums, k):

        seen = {0: 1}

        prefix_sum = 0
        count = 0

        for num in nums:

            prefix_sum += num

            need = prefix_sum - k

            if need in seen:
                count += seen[need]

            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
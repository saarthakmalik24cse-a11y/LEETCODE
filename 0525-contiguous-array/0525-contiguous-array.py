class Solution:
    def findMaxLength(self, nums):

        count = 0
        first_seen = {0: -1}
        max_length = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in first_seen:
                length = i - first_seen[count]
                max_length = max(max_length, length)
            else:
                first_seen[count] = i

        return max_length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
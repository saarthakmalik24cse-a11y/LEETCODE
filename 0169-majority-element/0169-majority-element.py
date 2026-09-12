class Solution:
    def majorityElement(self, nums):

        count = {}

        for num in nums:

            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        majority = nums[0]

        for num in count:
            if count[num] > count[majority]:
                majority = num

        return majority

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
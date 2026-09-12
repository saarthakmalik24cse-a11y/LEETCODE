class Solution:
    def moveZeroes(self, nums):

        slow = 0

        for fast in range(len(nums)):

            if nums[fast] != 0:

                nums[slow], nums[fast] = nums[fast], nums[slow]

                slow += 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
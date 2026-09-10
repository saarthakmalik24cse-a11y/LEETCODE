class NumArray:

    def __init__(self, nums):

        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)


    def sumRange(self, left, right):

        return self.prefix[right + 1] - self.prefix[left]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
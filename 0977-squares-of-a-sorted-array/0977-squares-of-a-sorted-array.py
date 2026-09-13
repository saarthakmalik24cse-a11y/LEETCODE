class Solution:
    def sortedSquares(self, nums):

        left = 0
        right = len(nums) - 1

        answer = [0] * len(nums)
        position = len(nums) - 1

        while left <= right:

            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                answer[position] = left_square
                left += 1
            else:
                answer[position] = right_square
                right -= 1

            position -= 1

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            groups = 1
            current = 0

            for x in nums:
                if current + x > mid:
                    groups += 1
                    current = 0

                current += x

            if groups <= k:
                right = mid
            else:
                left = mid + 1

        return left

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
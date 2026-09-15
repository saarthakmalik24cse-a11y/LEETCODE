class Solution:
    def firstBadVersion(self, n):

        left = 1
        right = n
        pAns=-1
        while left <= right:

            mid = (left + right) // 2

            if isBadVersion(mid):
                pAns=mid
                right = mid-1
            else:
                left = mid + 1

        return pAns

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
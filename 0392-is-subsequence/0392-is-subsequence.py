class Solution:
    def isSubsequence(self, s, t):

        left = 0
        right = 0

        while left < len(s) and right < len(t):

            if s[left] == t[right]:
                left += 1

            right += 1

        return left == len(s)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
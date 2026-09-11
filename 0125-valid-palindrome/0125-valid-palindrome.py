class Solution:
    def isPalindrome(self, s):

        clean = ""

        for char in s:
            if char.isalnum():
                clean += char.lower()

        left = 0
        right = len(clean) - 1

        while left < right:

            if clean[left] != clean[right]:
                return False

            left += 1
            right -= 1

        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
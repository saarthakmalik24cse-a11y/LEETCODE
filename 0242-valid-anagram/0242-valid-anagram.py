class Solution:
    def isAnagram(self, s, t):

        # If lengths are different,
        # they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create two empty hashmaps
        count_s = {}
        count_t = {}

        # Count characters of s
        for char in s:

            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        # Count characters of t
        for char in t:

            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

        # Compare both hashmaps
        return count_s == count_t

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
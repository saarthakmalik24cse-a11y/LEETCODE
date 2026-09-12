class Solution:
    def isAnagram(self, s, t):

    
        if len(s) != len(t):
            return False

       
        count_s = {}
        count_t = {}

       
        for char in s:

            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        
        for char in t:

            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

       
        return count_s == count_t

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
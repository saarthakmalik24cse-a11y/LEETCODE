class Solution:
    def findAnagrams(self, s: str, p: str):

        if len(p) > len(s):
            return []

        p_count = {}
        window = {}

        
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        result = []
        left = 0

        for right in range(len(s)):

            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

           
            if right - left + 1 > len(p):

                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

           
            if window == p_count:
                result.append(left)

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
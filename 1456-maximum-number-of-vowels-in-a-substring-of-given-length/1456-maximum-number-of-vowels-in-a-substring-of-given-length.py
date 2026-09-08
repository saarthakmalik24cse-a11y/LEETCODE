class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = "aeiou"

        count = 0

    
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # Slide the window
        for i in range(k, len(s)):

            # Remove character leaving the window
            if s[i - k] in vowels:
                count -= 1

            # Add new character entering the window
            if s[i] in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
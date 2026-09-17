class Solution :
    def canConstruct(self,ransomNote, magazine):

        count = {}

        for char in magazine:
            if char in count:
                count[char]+= 1
            else:
                count[char] = 1

        for char in ransomNote:
            if char not in count or count[char]==0:
                return False

            count[char] -=1

        return True



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution :
    def isAnagram(self,s,t):

        if len(s) != len(t):
            return False 

        count = {}

        for char in s :
            count[char] = count.get(char,0)+1
        for char in t :

            if char not in count :
                return False 
            
            count[char] -=1

            if count[char]<0:
                return False 
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
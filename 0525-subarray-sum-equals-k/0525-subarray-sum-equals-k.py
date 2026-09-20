class Solution:
    def subarraySum(self,nums,k):

        count = {0:1}
        prefix = 0
        answer = 0

        for num in nums:

            prefix += num
            if prefix - k in count:
                answer += count[prefix-k]

            count[prefix] = count.get(prefix,0)+1

        return answer 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
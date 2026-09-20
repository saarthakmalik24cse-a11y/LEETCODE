class Solution:
    def subarraysDivByK(self, nums, k):

        count = {0: 1}

        prefix = 0
        answer = 0

        for num in nums:

            prefix += num

            remainder = prefix % k

            if remainder in count:
                answer += count[remainder]

            count[remainder] = count.get(remainder, 0) + 1

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution :
    def numOfSubarrays(self,arr,k,threshold):

        target = k * threshold
        window = sum(arr[:k])

        answer = 0

        if window >= target:
            answer +=1

        for right in range(k,len(arr)):

            window += arr[right]
            window -= arr[right - k]

            if window >= target :
                answer += 1
        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
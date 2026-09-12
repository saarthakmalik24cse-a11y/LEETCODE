class Solution:
    def twoSum(self, nums, target):

        seen = {}                      

        for i in range(len(nums)):

            need = target - nums[i]     

            if need in seen:            
                return [seen[need], i]   

            seen[nums[i]] = i          



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
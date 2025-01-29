class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products and multiply with prefix
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

# for more info in leetcode: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

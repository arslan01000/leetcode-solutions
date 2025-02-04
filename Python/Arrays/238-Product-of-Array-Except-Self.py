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

# LeetCode 334: Increasing Triplet Subsequence  
# Check if there exists an increasing subsequence of length 3 in the array using O(n) time and O(1) space.

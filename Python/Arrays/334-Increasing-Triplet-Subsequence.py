class Solution:
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False


# LeetCode 334: Increasing Triplet Subsequence  
# Check if there exists an increasing subsequence of length 3 in the array using O(n) time and O(1) space.

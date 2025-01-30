class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        
        return result


# If the stack is empty, all brackets are matched correctly
# Return True if valid, False otherwise

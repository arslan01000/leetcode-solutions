class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        len1, len2 = len(word1), len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                merged.append(word1[i])
            if i < len2:
                merged.append(word2[i])
        return ''.join(merged)

# Problem: Merge two strings alternately, appending remaining characters from the longer string
# Link: https://leetcode.com/problems/merge-strings-alternately

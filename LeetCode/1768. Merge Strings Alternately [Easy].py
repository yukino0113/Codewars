"""
Runtime: 40ms, Beats 30.13% of users with Python3
Memory: 16.44 MB, Beats 96.51% of users with Python3
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        min_num = min(len(word1), len(word2))

        for i, j in zip(word1, word2):
            result.append(i)
            result.append(j)

        return ''.join(result) + word1[min_num:] + word2[min_num:]
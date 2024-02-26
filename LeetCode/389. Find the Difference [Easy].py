"""
45 ms, Beats 27.97% of users with Python3
16.57 MB, Beats 89.86% of users with Python3
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return ''.join([x for x in t if x not in s])

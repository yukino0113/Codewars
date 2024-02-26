"""
61 ms, Beats 17.35% of users with Python3
17.65 MB, Beats 42.04% of users with Python3
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
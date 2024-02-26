"""
36 ms, Beats 54.48% of users with Python3
16.46 MB, Beats 94.56% of users with Python3
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return len(haystack.split(needle)[0])

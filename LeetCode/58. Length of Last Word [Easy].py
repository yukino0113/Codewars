"""
31 ms, Beats 81.85% of users with Python3
16.47, MB Beats 99.25% of users with Python3
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([x for x in s.split(' ') if x][-1])

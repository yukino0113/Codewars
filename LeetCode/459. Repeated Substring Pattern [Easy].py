"""
152 ms, Beats 16.59% of users with Python3
16.90 MB, Beats 54.07% of users with Python3
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        if s[0] * len(s) == s:
            return True

        for i in range(1, len(s)):
            if s[:i] * (len(s) // i) == s:
                return True

        return False

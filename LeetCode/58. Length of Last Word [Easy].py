class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "" or s == " ":
            return 0

        val = s.split(' ')[-1]
        i = 0

        while val == '':
            try:
                val = s.split(' ')[-1 - i]
                i += 1
            except:
                return len(val)

        return len(val)
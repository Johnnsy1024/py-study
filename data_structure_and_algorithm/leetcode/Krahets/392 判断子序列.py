class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, j = 0, 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            if i == len(s):
                return True
        return False


so = Solution()
s = 'acb'
t = "ahbgdc"
print(so.isSubsequence(s, t))

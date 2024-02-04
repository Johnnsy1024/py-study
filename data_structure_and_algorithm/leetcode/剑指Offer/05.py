class Solution:
    def replaceSpace(self, s: str) -> str:
        s_ = s.split(' ')
        return '%20'.join(s_)

s = "We are happy."
s_ = Solution()
print(s_.replaceSpace(s))
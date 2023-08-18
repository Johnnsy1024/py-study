class Solution:
    def valid(self, s: str):
        flag = True
        l, r = 0, len(s) - 1
        while l<r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                flag = False
                break
        return flag

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        # if len(s) == 2:
        #     if s[0] == s[1]:
        #         return s
        #     else:
        #         return ''
        max_str = ''
        for i in range(len(s)):
            for j in range(len(s)):
                if self.valid(s[i:j+1]) and len(s[i:j+1])>len(max_str):
                    max_str = s[i:j+1]
        return max_str
    
s = Solution()
print(s.longestPalindrome("bbcddcbb"))
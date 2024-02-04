# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n <= 1:
#             return s
#         dp = [[False for _ in range(n)] for _ in range(n)]

#         max_len = 1
#         start = 0
#         for j in range(2, n):
#             for i in range(j):
#                 if j-i<=2:
#                     if s[i]==s[j]:
#                         dp[i][j] = True
#                         cur_len = j -i + 1
#                 else:
#                     if s[i]==s[j] and dp[i+1][j-1]:
#                         dp[i][j] = True
#                         cur_len = j-i+1
#                 if dp[i][j]:
#                     if cur_len > max_len:
#                         max_len = cur_len
#                         start = i
        
#         return s[start:start+max_len]
    
class Solution:
    def extend_left_and_right(self, left : int, right : int, s: str):
        # 左右指针不超过边界，左右指针所指数字相等，不满足任意一个条件
        # 所围成的子串都不是回文子串
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]
    
    def longestPalindrome(self, s: str) -> str:
        res = ''
        if not s:
            return ''
        for i in range(len(s)):
            condition_1 = self.extend_left_and_right(i, i, s)
            condition_2 = self.extend_left_and_right(i, i+1, s)
            
            if len(condition_1) > len(res):
                res = condition_1
            
            if len(condition_2) > len(res):
                res = condition_2
        
        return res
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        start, maxlen = 0, 1
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for length in range(2, len(s) + 1):
            for left in range(len(s)):
                right = left + length - 1
                if right >= len(s):
                    break
                if s[left] == s[right] and (length == 2 or dp[left+1][right-1]):
                    dp[left][right] = True
                    if length > maxlen:
                        start, maxlen = left, length
        return s[start: start + maxlen]
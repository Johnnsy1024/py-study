class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split(' ')
        s_list = [i for i in s_list if i!='']
        res = ' '.join(s_list[::-1])
        return res

nums = "a good   example"
s = Solution()
s.reverseWords(nums)
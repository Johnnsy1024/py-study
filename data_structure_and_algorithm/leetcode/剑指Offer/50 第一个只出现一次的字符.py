"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母
"""
"""
python 3.6 开始，默认的字典dict就是有序哈希，不用再使用collections中的OrderedDict了
"""
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = True
            else:
                dic[c] = False
        for k, v in dic.items():
            if v:
                return k 
        return " "

st = "leetcode"
s = Solution()
print(s.firstUniqChar(st))
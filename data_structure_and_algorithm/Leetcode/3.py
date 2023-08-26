from collections import deque


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_length = 0
        left, right = 0, 0
        tmp = ''
        while right < len(s):
            if s[right] not in tmp:
                tmp += s[right]
                max_length = max(max_length, len(tmp))
                right += 1
            else:
                left += 1
                right = left + 1
                tmp = s[left: right]
                max_length = max(max_length, len(tmp))
        return max_length


# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_length = 0
        q = deque()
        i = 0
        while i < len(s):
            if s[i] not in q:
                q.append(s[i])
                max_length = max(max_length, len(q))
                i += 1
            else:
                q.popleft()

        return max_length


string = 'abcabcbb'
s = Solution()
print(s.lengthOfLongestSubstring(string))

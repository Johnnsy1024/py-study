class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        left = s[:n]
        right = s[n:]
        def reverse(string):
            s = list(string)
            l, r = 0, len(string) - 1
            while l <= r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            return ''.join(s)
        left = reverse(left)
        right = reverse(right)
        new_s = left + right
        
        return reverse(new_s)
s = Solution()
print(s.reverseLeftWords("abcdefg", 3))
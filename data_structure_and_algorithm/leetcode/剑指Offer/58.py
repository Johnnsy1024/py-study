class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        tmp = s[:n]
        return s[n:]+tmp
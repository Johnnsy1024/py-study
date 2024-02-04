from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        res = set()
        if not s:
            return list(res)

        def dfs(tmp: list, res: list, used: set):
            if len(tmp) == len(s) and ''.join(tmp) not in res:
                res.add(''.join(tmp[:]))
                return

            for i in range(len(s)):
                if i not in used:
                    used.add(i)
                    tmp.append(s[i])
                    dfs(tmp, res, used)
                    used.discard(i)
                    tmp.pop()

        used = set()
        tmp = []
        dfs(tmp, res, used)
        return list(res)


if __name__ == '__main__':
    s = "abc"
    solution = Solution()
    print(solution.permutation(s))

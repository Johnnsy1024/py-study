from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res, path = [], []
        dig_to_letter = {
            2:['a', 'b', 'c'],
            3:['d', 'e', 'f'],
            4:['g', 'h', 'i'],
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r', 's'],
            8:['t', 'u', 'v'],
            9:['w', 'x', 'y', 'z']
        }
        def backtrack(start):
            if len(path) == len(digits):
                res.append(''.join(path[:]))
                return
            
            for i in range(start, len(digits)):
                letters = dig_to_letter[int(digits[i])]
                for j in range(len(letters)):
                    path.append(letters[j])
                    backtrack(i + 1)
                    path.pop()
        backtrack(0)
        
        return res

s = Solution()
print(s.letterCombinations("23"))
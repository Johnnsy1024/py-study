from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return
        i = 0
        while i + 1 < len(numbers):
            if numbers[i] <= numbers[i+1]:
                i += 1
            else:
                return numbers[i+1]
        return numbers[0]
    
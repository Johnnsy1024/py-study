import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr))
        return res
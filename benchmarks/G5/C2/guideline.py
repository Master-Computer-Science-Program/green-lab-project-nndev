from typing import List
import heapq
import sys

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
    
if __name__ == "__main__":
    s = Solution()
    points = [[i, i] for i in range(sys.argv[1])]
    print(s.kClosest(points, int(sys.argv[2])))
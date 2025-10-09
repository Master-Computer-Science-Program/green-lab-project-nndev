from typing import List
import heapq
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = sqrt((x ** 2) + (y ** 2))
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
    points = [[i, i] for i in range(int(config.C2_ARG[0]))]
    print(s.kClosest(points, int(config.C2_ARG[1])))
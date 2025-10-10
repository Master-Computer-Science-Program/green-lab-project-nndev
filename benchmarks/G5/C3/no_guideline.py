from typing import List
from collections import defaultdict
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def gcd(a, b):
            return gcd(b, a % b) if b else a

        res = 1
        for i in range(len(points) - 1):
            count = defaultdict(int)
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                slope = (dx, dy)
                count[slope] += 1
            res = max(res, max(count.values()) + 1)
        return res
    
if __name__ == "__main__":
    s = Solution()
    points = [[i, i] for i in range(int(config.C3_ARG[0]))]
    print(s.maxPoints(points))
from math import sqrt
import sys
import random

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqRoot = int(sqrt(num))
        return sqRoot * sqRoot == num
    
if __name__ == "__main__":
    s = Solution()
    for i in range(int(sys.argv[1])):
        n = random.randint(0, 10**10)
        print(s.isPerfectSquare(n))
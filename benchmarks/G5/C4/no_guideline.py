from math import sqrt
import sys

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqRoot = int(sqrt(num))
        return sqRoot * sqRoot == num
    
if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(int(sys.argv[1])))
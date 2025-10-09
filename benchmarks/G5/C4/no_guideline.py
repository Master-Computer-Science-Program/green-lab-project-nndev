from math import sqrt
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqRoot = int(sqrt(num))
        return sqRoot * sqRoot == num
    
if __name__ == "__main__":
    s = Solution()
    for i in range(int(config.C4_ARG[0])):
        print(s.isPerfectSquare(int(i)))
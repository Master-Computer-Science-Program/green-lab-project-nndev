import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r * r > num:
            r = (r + (num // r)) // 2
        return r * r == num
    
if __name__ == "__main__":
    s = Solution()
    for i in range(int(config.C4_ARG[0])):
        print(s.isPerfectSquare(int(i)))
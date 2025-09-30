import sys
import random

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r * r > num:
            r = (r + (num // r)) // 2
        return r * r == num
    
if __name__ == "__main__":
    s = Solution()
    for i in range(int(sys.argv[1])):
        n = random.randint(0, 10**10)
        print(s.isPerfectSquare(n))
import sys

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r * r > num:
            r = (r + (num // r)) // 2
        return r * r == num
    
if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(int(sys.argv[1])))
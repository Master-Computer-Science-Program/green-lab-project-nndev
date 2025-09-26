import sys

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n != 0 else 0
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
    
if __name__ == "__main__":
    s = Solution()
    print(s.tribonacci(int(sys.argv[1])))
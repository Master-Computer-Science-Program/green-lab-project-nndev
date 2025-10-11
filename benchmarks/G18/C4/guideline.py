import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time

class Solution:
    def __init__(self):
        self.dp = {}

    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n != 0 else 0
        if n in self.dp:
            return self.dp[n]

        self.dp[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.dp[n]
    
if __name__ == "__main__":
    start=time.time()
    s = Solution()
    loop=config.C4_ARG
    for i in loop:
        print(s.tribonacci(i))
    end=time.time()
    print("time: "+str(end-start))
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time


class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)
    
if __name__ == "__main__":
    s = Solution()
    loop=config.C3_ARG
    for i in loop:
        print(s.climbStairs(i))
  
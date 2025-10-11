from typing import List
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time
sys.setrecursionlimit(1000000)


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]

        return dfs(0)
    
if __name__ == "__main__":
    start=time.time()
    s = Solution()
    looparray=config.C5_ARG
    for i in looparray:
        print(s.rob(i))
    end=time.time()
    print(end-start)
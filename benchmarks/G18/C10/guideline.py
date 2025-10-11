from typing import List
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]

            memo[i][target] = (dfs(i + 1, target) or
                            dfs(i + 1, target - nums[i]))
            return memo[i][target]

        return dfs(0, target)
    
if __name__ == "__main__":
    start=time.time()
    s = Solution()
    looper=config.C9_ARG
    for i in looper:
        print(s.canPartition(i))
    end=time.time()
    print(end-start)

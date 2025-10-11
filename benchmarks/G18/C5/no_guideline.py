from typing import List
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time


class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(i):
            if i >= len(nums):
                return 0
            return max(dfs(i + 1),
                    nums[i] + dfs(i + 2))

        return dfs(0)
    
if __name__ == "__main__":
    s = Solution()
    looparray=config.C5_ARG
    for i in looparray:
        print(s.rob(i))

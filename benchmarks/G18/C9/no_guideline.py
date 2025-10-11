from typing import List
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, j):
            if i == len(nums):
                return 0

            LIS = dfs(i + 1, j) # not include

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) # include

            return LIS

        return dfs(0, -1)
    
if __name__ == "__main__":
    s = Solution()
    looper=config.C9_ARG
    for i in looper:
        print(s.lengthOfLIS(i))

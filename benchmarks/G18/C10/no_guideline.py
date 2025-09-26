from typing import List
import sys
import ast

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False

            return dfs(i + 1, target) or dfs(i + 1, target - nums[i])

        return dfs(0, sum(nums) // 2)
    
if __name__ == "__main__":
    s = Solution()
    print(s.canPartition(ast.literal_eval(sys.argv[1])))
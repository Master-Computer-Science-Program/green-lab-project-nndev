from typing import List
import sys
import ast

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
    print(s.rob(ast.literal_eval(sys.argv[1])))
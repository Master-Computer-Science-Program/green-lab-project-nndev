from typing import List
import sys
import ast

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = { 0 : 1 }

        def dfs(total):
            if total in memo:
                return memo[total]

            res = 0
            for num in nums:
                if total < num:
                    break
                res += dfs(total - num)
            memo[total] = res
            return res

        return dfs(target)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum4(ast.literal_eval(sys.argv[1]), int(sys.argv[2])))
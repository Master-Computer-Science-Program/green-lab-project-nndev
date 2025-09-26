from typing import List
import sys
import ast

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        def dfs(total):
            if total == 0:
                return 1

            res = 0
            for i in range(len(nums)):
                if total < nums[i]:
                    break
                res += dfs(total - nums[i])
            return res

        return dfs(target)

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum4(ast.literal_eval(sys.argv[1]), int(sys.argv[2])))

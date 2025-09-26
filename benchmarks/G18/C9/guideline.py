from typing import List
import sys
import ast

class Solution:
    def lengthOfLIS(self, nums: List[int]):
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            if i == n:
                return 0
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            LIS = dfs(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))

            memo[i][j + 1] = LIS
            return LIS

        return dfs(0, -1)
    
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS(ast.literal_eval(sys.argv[1])))
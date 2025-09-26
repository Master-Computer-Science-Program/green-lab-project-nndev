import sys

class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def dfs(target):
            if target == 0:
                return 0
            if target in memo:
                return memo[target]

            res = target
            for i in range(1, target + 1):
                if i * i > target:
                    break
                res = min(res, 1 + dfs(target - i * i))

            memo[target] = res
            return res

        return dfs(n)
    
if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(int(sys.argv[1])))
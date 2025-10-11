from typing import List
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
sys.setrecursionlimit(90000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(amount):
            if amount == 0:
                return 0

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins

if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange(config.C7_ARG[0],config.C7_ARG[1]))

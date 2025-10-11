from typing import List

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
import time

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
    start_time=time.time()
    looper=config.C1_ARG
    solution = Solution()
    for i in looper:
        print(solution.combinationSum4(i[0], int(i[1])))
    end_time=time.time()
    print(end_time-start_time)
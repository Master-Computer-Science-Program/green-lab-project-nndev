from typing import List
import sys
import ast

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, res = 0, len(nums) - 1, []

        while l <= r:
            if (nums[l] * nums[l]) > (nums[r] * nums[r]):
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1

        return res[::-1]
    
if __name__ == "__main__":
    from benchmarks.G2.config import C6_ARG
    s = Solution()
    for _ in range(15000000):
        s.sortedSquares(C6_ARG[0])

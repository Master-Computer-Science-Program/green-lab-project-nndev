from typing import List
import sys
import ast
import sys, os

class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        if nums[m] < target:
            return self.binary_search(m + 1, r, nums, target)
        return self.binary_search(l, m - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
    
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from config import C4_ARG
    s = Solution()
    for _ in range(15000000):
        s.search(C4_ARG[0], C4_ARG[1])

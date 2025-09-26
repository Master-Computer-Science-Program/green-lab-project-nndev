from typing import List
import sys
import ast

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
        nums.sort()
        return self.binary_search(0, len(nums) - 1, nums, target)
    
if __name__ == "__main__":
    s = Solution()
    print(s.search(ast.literal_eval(sys.argv[1]), int(sys.argv[2])))
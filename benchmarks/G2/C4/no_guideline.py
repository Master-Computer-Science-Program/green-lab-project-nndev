import sys
import ast

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # print("nums_arg:", nums)
        # nums.sort()
        nums = sorted(nums)
        # print(f"sorted: {nums}")
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        # print("nums:", nums)
        return l
    
if __name__ == "__main__":
    from benchmarks.G2.config import C4_ARG

    s = Solution()
    for _ in range(3): #1500000
        s.removeDuplicates(C4_ARG[0])

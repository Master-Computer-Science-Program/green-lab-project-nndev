import sys
import ast

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # print("nums_arg:", nums)
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        # print("nums:", nums)
        return l
    
if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from config import C4_ARG

    s = Solution()
    for _ in range(3):
        s.removeDuplicates(C4_ARG[0])

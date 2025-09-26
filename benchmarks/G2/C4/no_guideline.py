import sys
import ast

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums.sort()
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
    
if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates(ast.literal_eval(sys.argv[1])))
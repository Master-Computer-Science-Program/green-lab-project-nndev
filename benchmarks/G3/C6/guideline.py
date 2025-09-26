from typing import List
import sys
import ast

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
if __name__ == "__main__":
    s = Solution()
    print(s.hasDuplicate(ast.literal_eval(sys.argv[1])))
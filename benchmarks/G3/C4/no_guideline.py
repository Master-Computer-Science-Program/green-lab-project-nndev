from typing import List
import sys
import ast

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(ast.literal_eval(sys.argv[1]), int(sys.argv[2])))
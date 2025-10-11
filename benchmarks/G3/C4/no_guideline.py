from typing import List
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
if __name__ == "__main__":
    s = Solution()
    nums = list(range(config.C4_ARG[0]))
    target = nums[-2] + nums[-1]
    print(s.twoSum(nums, target))
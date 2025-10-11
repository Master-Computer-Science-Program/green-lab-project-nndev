from typing import List
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
if __name__ == "__main__":
    start_time=time.time()
    s = Solution()
    print(s.hasDuplicate(config.C6_ARG))
    end_time=time.time()
    print("time "+str(end_time-start_time))

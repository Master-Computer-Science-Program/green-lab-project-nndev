from typing import List
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        for i in range(n):
            cur_sum = 0
            for j in range(i, i + n):
                cur_sum += nums[j % n]
                res = max(res, cur_sum)

        return res
    
if __name__ == "__main__":
    start_time=time.time()
    s = Solution()
    print(s.maxSubarraySumCircular(config.C7_ARG))
    end_time=time.time()
    print("time: "+str(end_time-start_time))
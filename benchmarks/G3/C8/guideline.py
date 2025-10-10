from typing import List
import sys
import os
import ast
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arr = [1] * n
        rangei=range(n-1)
        for i in rangei:
            if ratings[i] == ratings[i + 1]:
                continue
            if ratings[i + 1] > ratings[i]:
                arr[i + 1] = arr[i] + 1
            elif arr[i] == arr[i + 1]:
                arr[i + 1] = arr[i]
                arr[i] += 1
                rangej=range(i - 1, -1, -1)
                for j in rangej:
                    if ratings[j] > ratings[j + 1]:
                        if arr[j + 1] < arr[j]:
                            break
                        arr[j] += 1

        return sum(arr)
    
if __name__ == "__main__":
    s = Solution()
    print(s.candy(config.C8_ARG))

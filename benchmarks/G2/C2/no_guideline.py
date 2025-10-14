from typing import List
import sys
import ast

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sort_num = sorted(numbers)
        for i in range(len(sort_num)):
            for j in range(i + 1, len(sort_num)):
                if sort_num[i] + sort_num[j] == target:
                    return [i + 1, j + 1]
        return []
    
if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from config import C2_ARG

    s = Solution()
    for _ in range(15000000):
        s.twoSum(C2_ARG[0], C2_ARG[1])

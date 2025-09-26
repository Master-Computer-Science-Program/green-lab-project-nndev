from typing import List
import sys
import ast

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
    
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(ast.literal_eval(sys.argv[1]), int(sys.argv[2])))
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
    
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([1,2,3,4], 3))
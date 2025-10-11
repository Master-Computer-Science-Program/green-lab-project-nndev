from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
    
if __name__ == "__main__":
    from benchmarks.G2.config import C2_ARG

    s = Solution()
    for _ in range(15000000):
        s.twoSum(C2_ARG[0], C2_ARG[1])

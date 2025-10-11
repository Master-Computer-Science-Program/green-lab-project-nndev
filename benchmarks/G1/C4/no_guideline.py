from typing import List


class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1

        if nums[(l + (r - l) // 2)] == target:
            return l + (r - l) // 2
        if nums[(l + (r - l) // 2)] < target:
            return self.binary_search((l + (r - l) // 2) + 1, r, nums, target)
        return self.binary_search(l, (l + (r - l) // 2) - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
    
if __name__ == "__main__":
    from benchmarks.G1.config import C4_ARG
    s = Solution()
    for _ in range(15000000):
        s.search(C4_ARG[0], C4_ARG[1])
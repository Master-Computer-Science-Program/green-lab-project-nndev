from typing import List
import sys
import ast

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.sort()
        nums2.sort()
        sort_nums1 = sorted(nums1)
        sort_nums2 = sorted(nums2)

        len1 = len(nums1)
        len2 = len(nums2)
        merged = sort_nums1 + sort_nums2

        merged.sort()
        totalLen = len(merged)
        if totalLen % 2 == 0:
            return (merged[totalLen // 2 - 1] + merged[totalLen // 2]) / 2.0
        else:
            return merged[totalLen // 2]

if __name__ == "__main__":
    from benchmarks.G2.config import C5_ARG

    s = Solution()
    for _ in range(15000000):
        s.findMedianSortedArrays(C5_ARG[0], C5_ARG[1])

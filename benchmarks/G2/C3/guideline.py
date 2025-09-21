class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        last = m + n - 1
        i, j = m - 1, n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1

            last -= 1

if __name__ == "__main__":
    s = Solution()
    nums1 = [10,20,20,40,0,0]
    s.merge(nums1, 4, [1,2], 2)
    print(nums1)
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
    # s = Solution()
    # print(s.merge(ast.literal_eval(sys.argv[1]), int(sys.argv[2]), ast.literal_eval(sys.argv[3]), int(sys.argv[4])))

    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from config import C3_ARG

    s = Solution()
    for _ in range(80000000):
        s.merge(C3_ARG[0], C3_ARG[1], C3_ARG[2], C3_ARG[3])

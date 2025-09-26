import sys

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        ls = len(s)
        for i in range(ls):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
    
if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram(sys.argv[1], sys.argv[2]))
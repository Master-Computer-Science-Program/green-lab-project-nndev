import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

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
    for i in range(config.C5_ARG[0]):
        print(s.isAnagram(config.C5_ARG[1], config.C5_ARG[2]))
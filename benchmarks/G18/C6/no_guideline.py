import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 

class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            res = dfs(i + 1)
            if i < len(s) - 1:
                if (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                    res += dfs(i + 2)

            return res

        return dfs(0)
    
if __name__ == "__main__":
    s = Solution()
    s = Solution()
    looparray=config.C6_ARG
    for i in looparray:
        print(s.numDecodings(i))

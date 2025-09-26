from typing import List
import sys
import ast

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(i):
            if i == len(s):
                return True

            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                    s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        return True
            return False

        return dfs(0)
    
if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak(sys.argv[1], ast.literal_eval(sys.argv[2])))
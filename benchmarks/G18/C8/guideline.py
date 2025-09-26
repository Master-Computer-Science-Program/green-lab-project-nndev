from typing import List
import sys
import ast

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]

            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                    s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)
    
if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak(sys.argv[1], ast.literal_eval(sys.argv[2])))
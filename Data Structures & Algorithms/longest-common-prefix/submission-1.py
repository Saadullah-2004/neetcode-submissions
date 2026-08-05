class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key=len)
        index = strs.index(prefix)
        res = ""
        for i in range(len(prefix)):
            for s in strs:
                if i == len(prefix) or s[i] != strs[index][i]:
                    return res
            res += strs[index][i]
        return res
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = min(strs, key=len)
        new = prefix
        for s in strs:
            for i in range(len(prefix)):
                if i >= len(s) or prefix[i] != s[i]:
                    temp = prefix[:i]
                    if len(temp) < len(new):
                        new = temp
                    break
        return new
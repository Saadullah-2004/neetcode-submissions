class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        i = 0
        y = 1
        length = 1
        temp = 1
        visited = {s[0]}
        while y < len(s):
            if s[y] not in visited:
                temp += 1
                length = max(length, temp)
                visited.add(s[y])
                y += 1
            else:
                visited.remove(s[i])
                i += 1
                temp -= 1
        return length

                

        
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Now instead of having deadicated lists we have track the total character by using ord
        from collections import defaultdict
        ans = defaultdict(list)

        for strings in strs:
            anagram = [0] * 26
            for char in strings:
                anagram[ord(char) - 97] +=1
            ans[tuple(anagram)].append(strings)

        final = []
        for group in ans.keys():
            final.append(ans[group])

        return final
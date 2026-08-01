class Solution:

    def encode(self, strs: List[str]) -> str:
        delimter = "#"
        ret = str(len(strs)) + delimter
        for s in strs:
            length = len(s)
            ret += str(length) + delimter + s
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        y = 0
        num_s = ""
        while s[y] != "#":
            num_s += s[y]
            y+=1
        y += 1
        num_s = int(num_s)
        final = []
        for i in range(num_s):
            length = ""
            while s[y] != "#":
                length += s[y]
                y+=1
            print(length)
            length = int(length)
            final.append(s[y + 1: y + length + 1])
            y += length + 1
        return final




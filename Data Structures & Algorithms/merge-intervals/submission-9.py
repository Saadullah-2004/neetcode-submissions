class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        match = False
        intervals.sort(key=lambda interval: interval[1])
        intervals.sort(key=lambda interval: interval[0])
        start, end = intervals[0][0], intervals[0][1]
        print(intervals)
        for i in range(len(intervals) - 1):
            s, e = intervals[i + 1][0], intervals[i + 1][1]
            # If the intervals overlap
            if end >= s:
                final_e = e if e > end else end
                new = [start, final_e]
                end = final_e
                match = True
 
            else:
                if match:
                    res.append(new)
                    match = False
                else:
                    res.append([start, end])
                start = s
                end = e


        if match:
            res.append(new)
        else:
            res.append([start, end])

        return res
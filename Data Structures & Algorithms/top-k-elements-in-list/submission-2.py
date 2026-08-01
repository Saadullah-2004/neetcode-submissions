class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        answer = defaultdict(int)
        
        for i in range(len(nums)):
            answer[nums[i]] += 1

        new = [[] for i in range(len(nums) + 1)] 


        for i in answer.keys():
            count = answer[i]

            new[count].append(i)


        ret = []
        for i in range(len(new)):
            x = new.pop()
            if x:
                ret.extend(x)
            if len(ret) == k:
                return ret
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        if not intervals:
            result.append(newInterval)
            return result
        for i,n in enumerate(intervals):
            if n[1] < newInterval[0]:
                result.append(n)
            elif n[0] > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            else:
                newInterval[0] = min(newInterval[0],n[0])
                newInterval[1] = max(newInterval[1],n[1])
        result.append(newInterval)
        return result
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        max_day = max(n[1] for n in events)
        heap = []
        e = 0
        count = 0
        n = len(events)
        for i in range(1,max_day+1):
            while e<n and i== events[e][0]:
                heapq.heappush(heap,events[e][1])
                e+=1
            while heap and heap[0] < i:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                count+=1
            if e==n and not heap:
                break
        return count
                

          
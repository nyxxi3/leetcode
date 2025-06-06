import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for n in points:
            dist = n[0] ** 2 + n[1] ** 2
            heapq.heappush(heap,(-dist, n))
            if len(heap) > k:
                heapq.heappop(heap)
       
       
        return [p for (_,p) in heap]

from typing import List, Optional
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        if max_heap is None:
            return 0
        while max_heap and len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            rock = simulate(x,y)
            if rock is not None:
                heapq.heappush(max_heap,rock)
           

        if len(max_heap) == 1:
                return max_heap[0] * -1
            
        if not max_heap:
            return 0

       
def simulate(x:int,y:int) -> Optional[int]:
        if x == y:
            return None
        return -1* (abs(x) - abs(y))

# Problem link: https://leetcode.com/problems/k-closest-points-to-origin/
import heapq as pq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            # Distance from origin
            dist = -(x*x + y*y)
            if len(heap) == K:
                pq.heappushpop(heap, (dist,x,y))
            else:
                pq.heappush(heap, (dist,x,y))
                
        return[[x,y] for (dist, x, y) in heap]
        

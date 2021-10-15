# Min Cost to Connect All Points
# Minheap + Primsalgo O(n^2logn)

# Frontier - Minheap , Visit set - avoid cycle

from typing import List
import heapq
# Build an Adjacency List first
# [Cost,node]
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        N = len(points)
        adj = {i:[] for i in range(N)}
        
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = abs(x2-x1)+abs(y2-y1)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        #Prims Algorithm      
        res = 0
        minH = [[0,0]]
        visit = set()
        while(len(visit)<N):
            
            cost , node = heapq.heappop(minH)
            
            if node in visit:
                continue
            res+= cost
            visit.add(node)
            for neiCost,neig in adj[node]:
                if neig not in visit:
                    heapq.heappush(minH,[neiCost,neig])
                    
        return res
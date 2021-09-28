# Network Delay Time Problem
# Dijakstra + BFS(Minheap) - O(ElogV)
from typing import List
import heapq
import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
            
        visit = set()
        minHeap = [(0,k)]
        t = 0
        
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t,w1)
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2))
            
        return t if len(visit) == n else -1
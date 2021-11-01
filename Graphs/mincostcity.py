# Connecting Cities With Minimum Cost Problem (Asked in amazon & American Express)
# Union Find and Krushkals Algorithm(MST)
# O(nlogn) Time Complexity

def minCost(N,connections):
    uf = dict()
    # Find Parent node 
    # Initially node is parent to itself & find parent node using Union Find
    def parent(node,uf):
        if node not in uf:
            uf[node] = node
            return node
        else :
            while uf[node] != node:
                node = uf[node]
            return node
    # Sort on the basis of Cost
    connections.sort(key = lambda x: x[2])
    result = 0
    
    for i,j,cost in connections:
        p1,p2 = parent(i,uf),parent(j,uf)
        
        if p1 != p2:
            N-=1
            uf[p1] = p2
            result += cost
    return result if N==1 else -1
    
print(minCost(3,[[1,2,5],[1,3,5],[2,3,1]]))
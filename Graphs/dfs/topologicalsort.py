# Topological sort O(V+E) approach
from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.graph = defaultdict(list)
        self.V = v 
    def addEdge(self,m,n):
        self.graph[m].append(n)

    def sortUtil(self,v,visited,stack):
        visited[v] = True

        for element in self.graph[v]:
            if visited[element] == False:
                self.sortUtil(element,visited,stack)
        stack.insert(0,v)
    
    def topSort(self):
        visited = [False]*self.V
        stack = []

        for element in range(self.V):
            if visited[element] == False:
                self.sortUtil(element,visited,stack)
        print(stack)
    
graph = Graph(5)
graph.addEdge(0,1);
graph.addEdge(0,3);
graph.addEdge(1,2);
graph.addEdge(2,3);
graph.addEdge(2,4);
graph.addEdge(3,4);

print("Topological Sort :")
graph.topSort()
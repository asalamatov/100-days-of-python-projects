"""
Adjacency List - Directed Graph
"""

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        # v1=>[v2,v3,v4]

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def printGraph(self):
        for node in self.graph:
            for v in self.graph[node]:
                print(node, "=>", v)

g = Graph()
g.insertEdge(1,5)
g.insertEdge(5,2)
g.insertEdge(2,7)
g.insertEdge(7,1)

g.printGraph()
# 1 => 5
# 5 => 2
# 2 => 7
# 7 => 1
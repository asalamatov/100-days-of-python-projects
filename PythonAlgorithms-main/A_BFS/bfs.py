from collections import defaultdict, deque
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def BFS(self, startNode):
        q = deque([startNode])
        visited = set()
        visited.add(startNode)
        print(startNode, end="=>")
        while q:
            v = q.popleft()
            for n in self.graph[v]:
                if n not in visited:
                    q.append(n)
                    visited.add(n)
                    print(n, end="=>")

g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(8,9)

g.BFS(2)

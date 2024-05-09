class Graph:
    def __init__(self):
        self.graph = list()

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if not visited[i]:
                self.DFS(i, visited)

if __name__ == "__main__":
    g = Graph()
    instances = int(input())
    for i in range(instances):
        g = Graph()
        nodes = int(input())
        node = list()
        for j in range(nodes):
            line = input()
            node[j] = line[0]
            for k in range(1,len(line)):
                if line[k] != " ":
                    g.addEdge(node, line[k])
        visited = [False] * len(g.graph)
        g.DFS(node[0], visited)    
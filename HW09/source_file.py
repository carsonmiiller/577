# returns the maximum flow from s to t in G
def maxFlow(s, t, G):

    # returns true if there is a path from s to t in residual graph G, false otherwise
    def bfs(s, t, parent):
        # mark all nodes as not visited
        visited = [False] * len(G)

        # create a queue for BFS
        queue = [s]

        # mark starting node as visited
        visited[s] = True

        # keep looping until queue is empty
        while queue:
            u = queue.pop(0)
            for v, capacity in enumerate(G[u]):
                # add unvisited nodes to queue if there is capacity along edge (u, v) and track parent of v
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
        return visited[t]
    
    # returns the maximum flow in G from s to t
    def FF(s, t):
        # set path and flow to "null"
        parent = [-1] * len(G)
        maxFlow = 0

        # while there is a path from s to t in G
        while bfs(s, t, parent):
            pathFlow = float('Inf')
            curr = t

            # follow parent back from t to s
            while curr != s:
                # capture bottleneck along path
                pathFlow = min(pathFlow, G[parent[curr]][curr])
                curr = parent[curr]

            # add bottleneck length along path to maxFlow
            maxFlow += pathFlow
            v = t

            # update residual graph
            while v != s:
                u = parent[v]
                G[u][v] -= pathFlow
                G[v][u] += pathFlow
                v = parent[v]

        return maxFlow
    
    return FF(s, t)

instances = int(input())
for i in range(instances):
    numNodes, numEdges = map(int, input().split(" "))
    # create graph G = (V, E) with num_nodes nodes and num_edges edges in an adjecency matrix where G[u][v] = c means that there is an edge (u, v) with capacity c
    G = [[0 for i in range(numNodes)] for j in range(numNodes)]

    for j in range(numEdges):
        u, v, c = map(int, input().split(" "))
        # add edge (u, v) with capacity c to G
        G[u-1][v-1] += c

    print(maxFlow(0, numNodes - 1, G))
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y): 
    if rank[x] < rank[y]: 
        parent[x] = parent[y] 
    elif rank[x] > rank[y]: 
        parent[y] = parent[x] 
    else: 
        parent[y] = parent[x] 
        rank[x] += 1

def kruskal(graph, V):
    result = []
    i, e = 0, 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(V):
        parent.append(node)
        rank.append(0)
    
    while e < V - 1:
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    
    print("Minimum Spanning Tree:")
    for u, v, weight in result:
        print(f"{u} -- {v} == {weight}")

V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))
graph = []

for _ in range(E):
    u, v, w = map(int, input("Enter edge (u v w): ").split())
    graph.append([u, v, w])

kruskal(graph, V)

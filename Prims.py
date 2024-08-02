def prims_algorithm(graph, start_vertex):
    V = len(graph)  # Number of vertices in the graph
    visited = [False] * V  # To keep track of visited vertices
    min_heap = [(0, start_vertex)]  # Min-heap initialized with the start vertex and cost 0
    mst_cost = 0  # Total cost of MST
    mst_edges = []  # List to store edges in the MST

    while min_heap:
        cost, u = heapq.heappop(min_heap)  # Extract the vertex with the minimum cost
        
        if visited[u]:
            continue  # If already visited, skip to the next iteration

        visited[u] = True  # Mark the current vertex as visited
        mst_cost += cost  # Add the cost to the total MST cost
        
        if cost != 0:
            mst_edges.append((u, cost))  # Append the edge to the MST edges list

        for v, weight in graph[u]:  # Iterate over the adjacent vertices
            if not visited[v]:  # If the vertex is not visited
                heapq.heappush(min_heap, (weight, v))  # Push the edge to the heap
    
    return mst_cost, mst_edges  # Return the total MST cost and the edges in the MST


def main():
    V = int(input("Enter the number of vertices: "))
    graph = [[] for _ in range(V)]

    E = int(input("Enter the number of edges: "))
    for _ in range(E):
        print("Enter edge and weight (e.g., '0 1 10' for an edge between 0 and 1 with weight 10):")
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))  # Because the graph is undirected

    start_vertex = int(input("Enter the starting vertex: "))

    mst_cost, mst_edges = prims_algorithm(graph, start_vertex)
    print("\nMinimum Spanning Tree cost:", mst_cost)
    print("Edges in the MST:", mst_edges)

if __name__ == "__main__":
    main()

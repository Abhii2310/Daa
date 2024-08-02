import time

def DFS(graph, visited, vertex):
    visited[vertex] = True
    print(vertex)
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            DFS(graph, visited, neighbor)

def main():
    vertices = input("Enter the vertices separated by spaces: ").split()
    V = len(vertices)
    
    vertex_index = {vertex: i for i, vertex in enumerate(vertices)}
    
    graph = {vertex: [] for vertex in vertices}
    
    E = int(input("\nEnter the number of edges: "))
    for i in range(E):
        print(f"Enter edge {i+1} separated by spaces: ")
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)  # Remove this line if the graph is directed
    
    print("\nAdjacency list: ")
    for vertex in graph:
        print(f"{vertex}: {graph[vertex]}")
    
    start = input("\nEnter the start vertex: ")
    visited = {vertex: False for vertex in vertices}
    
    start_time = time.time()
    print("\nDFS: ")
    DFS(graph, visited, start)
    end_time = time.time()
    
    print(f"\nTime taken for DFS: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()


def dsr(graph, source, destination):
    """
    Simulates the Dynamic Source Routing (DSR) route discovery process.
    
    Args:
    - graph: A list of lists representing the adjacency list of the graph.
    - source: The source node from which the route discovery process starts.
    - destination: The destination node to which the route is being discovered.
    
    Returns:
    - path: A list containing the shortest paths from the source to each node.
    """
    # Initialize the route discovery process
    path = [None] * len(graph)
    path[source] = [source]  # Start with the source node's path being itself
    queue = [source]  # Initialize the queue with the source node
    while queue:
        node = queue.pop(0)  # Dequeue the first node from the queue
        graph[node].sort()  # Sort the neighbors of the current node lexicographically
        for neighbor in graph[node]:
            # If the neighbor is the destination, skip it
            if neighbor == destination:
                continue
            # Update the path if the neighbor has no path or the new path is shorter
            if path[neighbor] is None or len(path[neighbor]) > len(path[node]) + 1:
                path[neighbor] = path[node] + [neighbor]  # Update the path to neighbor
                queue.append(neighbor)  # Enqueue the neighbor for further exploration
    return path

def main():
    # Read input: number of vertices, number of edges, and the graph
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # Print the graph
    print("Graph:")
    for i in range(1, n + 1):
        print(i, "-->", graph[i])
    # Read source and destination nodes
    source, destination = map(int, input().split())
    # Execute DSR route discovery process
    path = dsr(graph, source, destination)
    print("-----------------")
    # Print the paths forwarded in RREQ for each vertex
    for i in range(1, n + 1):
        if path[i]:
            print(" ".join(map(str, path[i])))
        else:
            print(-1)
            
if __name__ == '__main__':
    main()
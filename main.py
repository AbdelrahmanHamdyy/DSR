def dsr(graph, source, destination):
    print("Source:", source)
    print("Destination:", destination)
    path = [None] * len(graph)
    path[source] = [source]
    queue = [source]
    while queue:
        node = queue.pop(0)
        graph[node].sort()
        for neighbor in graph[node]:
            if neighbor == destination:
                continue
            if path[neighbor] is None or len(path[neighbor]) > len(path[node]) + 1:
                path[neighbor] = path[node] + [neighbor]
                queue.append(neighbor)
    print("Path:", path)
    return path

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print("Graph:")
    for i in range(1, n + 1):
        print(i, "-->", graph[i])
    source, destination = map(int, input().split())
    path = dsr(graph, source, destination)
    print("-----------------")
    for i in range(1, n + 1):
        if path[i]:
            print(" ".join(map(str, path[i])))
        else:
            print(-1)
            
if __name__ == '__main__':
    main()
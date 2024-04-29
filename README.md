# DSR

### Dynamic Source Routing is a routing protocol used in wireless ad hoc networks. The DSR protocol is designed to find and maintain routes between nodes in a wireless network, without the need for a centralized routing infrastructure.

In DSR, when a source node wants to send a packet to a destination node, it first searches its route cache for a route to the destination. If a route is not found, the source node initiates a route discovery process. During route discovery, the source node broadcasts a route request packet, which is received by its neighbors. Each neighbor forwards the packet to its neighbors, until the packet reaches the destination or a node that has a route to the destination in its cache. The route discovery process creates a route from the source to the destination, which is added to the route cache of all nodes along the path. Once a route has been established, packets can be sent between the source and destination using the discovered route.

_In this challenge, you will simulate the DSR route discovery process._

Given a graph of n vertices and m bidirectional edges. Each node has no prior knowledge of the network topology (there is no cached routes).

Then two vertices are given, your task is to initiate the route discovery process from the source to the destination. Each vertex should broadcast the RREQ (route request) to the neighboring vertices. Output the path forwarded in the RREQ.

<hr>

### Input Format

The first line consists of two integers n and m - the number of vertices and the number of edges.

Each of the following m lines contains a pair of integers x and y, that show that an edge exists between vertices x and y. For each pair of vertices there will be at most one edge between them, no edge connects a vertex to itself.

The next line contains a pair of integers source u and destination v, asking about the route between them.

### Constraints

2 ≤ n ≤ 1000

1 ≤ m ≤ (n.(n-1)) / 2

1 ≤ x, y ≤ n, x ≠ y

1 ≤ u, v ≤ n, u ≠ v

### Output Format

Output n lines. The i th line represents the path forwarded in RREQ for vertex i - (1 ≤ i ≤ n).

`If there are multiple possible paths, output the shortest one having the lexicographically smallest path. If a vertex won't forward a RREQ, output -1.`

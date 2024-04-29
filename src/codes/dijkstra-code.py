def dijkstra_shortest_path(n: i32, source: i32) -> i32:
    i: i32; j: i32; v: i32; u: i32; mindist: i32; alt: i32; dummy: i32; uidx: i32
    dist_sum: i32;
    graph: dict[i32, i32] = {}
    dist: dict[i32, i32] = {}
    prev: dict[i32, i32] = {}
    visited: dict[i32, bool] = {}
    Q: list[i32] = []

    for i in range(n):
        for j in range(n):
            graph[n * i + j] = abs(i - j)

    for v in range(n):
        dist[v] = 2147483647
        prev[v] = -1
        Q.append(v)
        visited[v] = False
    dist[source] = 0

    while len(Q) > 0:
        u = -1
        mindist = 2147483647
        for i in range(len(Q)):
            if mindist > dist[Q[i]]:
                mindist = dist[Q[i]]
                u = Q[i]
                uidx = i
        dummy = Q.pop(uidx)
        visited[u] = True

        for v in range(n):
            if v != u and not visited[v]:
                alt = dist[u] + graph[n * u + v]

                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    dist_sum = 0
    for i in range(n):
        dist_sum += dist[i]
    return dist_sum
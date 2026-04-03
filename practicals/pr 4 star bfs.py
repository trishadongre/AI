import heapq, time
from collections import deque

# Graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'G': 5},
    'D': {'G': 1},
    'G': {}
}

heuristic = {'A': 6, 'B': 4, 'C': 3, 'D': 1, 'G': 0}

# A* Algorithm
def astar(start, goal):
    t = time.time()
    pq = [(0, start)]
    cost = {start: 0}
    while pq:
        _, n = heapq.heappop(pq)
        if n == goal: break
        for nb, w in graph[n].items():
            c = cost[n] + w
            if nb not in cost or c < cost[nb]:
                cost[nb] = c
                heapq.heappush(pq, (c + heuristic[nb], nb))
    return cost[goal], time.time() - t

# BFS Algorithm
def bfs(start, goal):
    t = time.time()
    q, v = deque([start]), {start}
    while q:
        n = q.popleft()
        if n == goal: break
        for nb in graph[n]:
            if nb not in v:
                v.add(nb)
                q.append(nb)
    return time.time() - t

# Run
a_cost, a_time = astar('A', 'G')
b_time = bfs('A', 'G')

print("A* Cost:", a_cost, "Time:", a_time)
print("BFS Time:", b_time)

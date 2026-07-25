import heapq

def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start))

    came_from = {}
    g_score = {start: 0}

    closed = set()

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        if current in closed:
            continue

        closed.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed:
                continue

            tentative_g = g + cost

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                f_score = tentative_g + heuristics[neighbor]
                heapq.heappush(open_list, (f_score, tentative_g, neighbor))

    return None


# -------- Input --------

n, m = map(int, input().split())

graph = {}

for _ in range(m):
    u, v, w = input().split()
    w = int(w)

    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))

heuristics = {}

for _ in range(n):
    node, h = input().split()
    heuristics[node] = int(h)

start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")

path = a_star(graph, heuristics, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found")
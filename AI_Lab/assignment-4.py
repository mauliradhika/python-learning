import heapq

def uniform_cost_search(graph, start, goal):
    pq = []  
    heapq.heappush(pq, (0, start, [start]))
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return None, None


graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('D', 4)],
    'C': [('A', 5), ('D', 1)],
    'D': [('B', 4), ('C', 1), ('E', 3)],
    'E': []
}

start = 'A'
goal = 'E'

cost, path = uniform_cost_search(graph, start, goal)
print("Cost:", cost)
print("Path:", path)

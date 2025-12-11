import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_first_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = [] 
    
    heapq.heappush(pq, (manhattan(start, goal), start))
    visited = set()

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while pq:
        h, (x, y) = heapq.heappop(pq)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == goal:
            return f"Treasure found at {goal}! Nodes visited: {len(visited)}"

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if (nx, ny) not in visited:
                    heapq.heappush(pq, (manhattan((nx, ny), goal), (nx, ny)))

    return "Treasure not found."
    
grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

start = (0,0)
goal = (2,3)

print(best_first_search(grid, start, goal))
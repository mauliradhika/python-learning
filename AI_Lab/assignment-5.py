import heapq

start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    x, y = divmod(zero_index, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_index = nx * 3 + ny
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = \
                new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))

    return neighbors

def uniform_cost_search(start, goal):
    priority_queue = [(0, start, [])]  
    visited = set()
    nodes_explored = 0

    while priority_queue:
        cost, state, path = heapq.heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]
        nodes_explored += 1

        if state == goal:
            return path, cost, nodes_explored

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(priority_queue,
                               (cost + 1, neighbor, path))

    return None, float('inf'), nodes_explored

if __name__ == "__main__":
    path, cost, nodes = uniform_cost_search(start_state, goal_state)

    print("Solution Depth:", len(path) - 1)
    print("Total Cost:", cost)
    print("Nodes Explored:", nodes)

    print("\nSolution Path:")
    for state in path:
        print(state)

import random

def calculate_conflicts(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or \
               abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_neighbors(state):
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = state[:]
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

def hill_climbing():
    n = 8
    current = [random.randint(0,7) for _ in range(n)]
    while True:
        current_conflict = calculate_conflicts(current)
        neighbors = get_neighbors(current)
        next_state = current
        min_conflict = current_conflict
        for neighbor in neighbors:
            conflict = calculate_conflicts(neighbor)
            if conflict < min_conflict:
                min_conflict = conflict
                next_state = neighbor
        if next_state == current:
            return current, current_conflict
        current = next_state

solution, conflicts = hill_climbing()
print("Solution:", solution)
print("Conflicts:", conflicts)
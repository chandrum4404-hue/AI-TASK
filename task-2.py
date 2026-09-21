import heapq

# Graph
graph = {
    'S': [('A', 3), ('C', 2)],
    'A': [('B', 4)],
    'B': [('D', 5)],
    'C': [('D', 2)],
    'D': []
}

#! Heuristic search

h = {
    'S': 4,
    'A': 7,
    'B': 5,
    'C': 2,
    'D': 0
}

def a_star(start, goal):
    # Priority queue: (f, g, node, path)
    open_list = [(h[start], 0, start, [start])]

    visited = set()

    print("Nodes explored:")
    print()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        print("Node:", current)
        print("g =", g)
        print("h =", h[current])
        print("f =", f)
        print()

        # Goal reached
        if current == goal:
            return path, g

        # Explore neighbours
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float('inf')


# Run A*
start = 'S'
goal = 'D'

path, total_cost = a_star(start, goal)

print("Final Path:", " -> ".join(path))
print("Total Cost:", total_cost)



#! Hill climbing search

def f(x):
    return (x - 5) ** 2 + 10


# Initial value
x = 0
step = 1

print("Hill Climbing Search")
print("--------------------")

while True:
    current_value = f(x)

    # Generate neighbouring values
    left = x - step
    right = x + step

    left_value = f(left)
    right_value = f(right)

    print("x =", x, "f(x) =", current_value)

    # Find better neighbour
    if left_value < current_value:
        x = left

    elif right_value < current_value:
        x = right

    else:
        break


print()
print("Approximate Minimum x =", x)
print("Minimum f(x) =", f(x))
def a_star(start, goal, graph):
    open_list = [start]
    closed_list = set()
    g_values = {start: 0}
    parents = {start: None}

    while open_list:
        current = min(open_list, key=lambda x: g_values[x] + heuristic(x, goal))
        open_list.remove(current)

        if current == goal:
            return reconstruct_path(parents, current), g_values[goal]

        closed_list.add(current)

        for neighbor in graph[current]:
            if neighbor in closed_list:
                continue

            tentative_g = g_values[current] + distance(current, neighbor)

            if neighbor not in open_list or tentative_g < g_values[neighbor]:
                open_list.append(neighbor)
                g_values[neighbor] = tentative_g
                parents[neighbor] = current

    return None, None  # No path found

def reconstruct_path(parents, current):
    path = [current]
    while parents[current] is not None:
        current = parents[current]
        path.append(current)
    return path[::-1]
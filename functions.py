from collections import deque

def bfs(maze):
    start = maze.start
    goal = maze.goal

    queue = deque([start])
    visited = set([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for neighbor in maze.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

    # مسیر رو بازسازی می‌کنیم
    if goal not in came_from:
        return None  # راه نداره

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path


def mark_path(maze, path):
    for (r, c) in path:
        if maze.maze[r][c] not in ("S", "G"):
            maze.maze[r][c] = "*"

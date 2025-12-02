class Maze:
    def __init__(self, file_path):
        with open(file_path, "r") as f:
            content = f.read().splitlines()

        self.maze = [list(row) for row in content]

        self.start = None
        self.goal = None

        for r in range(len(self.maze)):
            for c in range(len(self.maze[r])):
                if self.maze[r][c] == "S":
                    self.start = (r, c)
                elif self.maze[r][c] == "G":
                    self.goal = (r, c)

        if not self.start or not self.goal:
            raise ValueError("Maze must contain S and G positions.")

    def neighbors(self, position):
        r, c = position
        options = []

        moves = [(0,1), (0,-1), (1,0), (-1,0)]

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if self.maze[nr][nc] != "#":
                options.append((nr, nc))

        return options

    def display(self):
        for row in self.maze:
            print("".join(row))


m = Maze("maze.txt")
print("Start:", m.start)
print("Goal:", m.goal)
print("Neighbors of start:", m.neighbors(m.start))

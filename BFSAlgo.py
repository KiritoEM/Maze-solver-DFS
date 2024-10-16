from collections import deque

class BFS:
    def __init__(self):
        self.maze = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.queue = deque()
        self.visited = [[False] * len(self.maze[0]) for _ in range(len(self.maze))]
        self.path = []
        self.finished = False

    def solve(self, start_x, start_y, des_x, des_y):
        self.visited[start_x][start_y] = True
        self.queue.append((start_x, start_y))

        while len(self.queue) > 0 and not self.finished:
            (curr_x, curr_y) = self.queue.popleft()  # Dequeue the current position
            print(f"Visiting: {(curr_x, curr_y)}")

            if curr_x == des_x and curr_y == des_y:
                self.path.append((curr_x, curr_y))
                self.finished = True
                return

            neighbors = self.check_neighbors(curr_x, curr_y)

            for n_x, n_y in neighbors:
                if not self.visited[n_x][n_y] and self.maze[n_x][n_y] == 0:
                    self.visited[n_x][n_y] = True
                    self.queue.append((n_x, n_y))
                    self.path.append((n_x, n_y))

    def check_neighbors(self, x, y):
        neighbors = []
        directions = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]

        for nx, ny in directions:
            if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]) and self.maze[nx][ny] == 0:
                neighbors.append((nx, ny))

        return neighbors

    def print_solution(self):
        if self.finished:
            print("Path found:")
            for pos in self.path:
                print(pos)
        else:
            print("Destination is inaccessible.")

        print("\nVisited matrix:")
        for row in self.visited:
            print(' '.join(['1' if cell else '0' for cell in row]))
        print()

bfs = BFS()
start_x, start_y = 0, 0
des_x, des_y = 4, 4
bfs.solver(start_x, start_y, des_x, des_y)
bfs.print_solution()

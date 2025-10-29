def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    return path[::-1]

class PriorityQueue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not self.items
    def push(self, item, priority):
        for i, (_, p) in enumerate(self.items):
            if priority < p:
                self.items.insert(i, (item, priority))
                return
        self.items.append((item, priority))
    def pop(self):
        return self.items.pop(0)[0]

def a_star(grid, start, goal):
    open_set = PriorityQueue()
    open_set.push(start, 0)
    came_from = {}
    g_score = {start: 0}
    visited = set()
    while not open_set.is_empty():
        current = open_set.pop()
        if current == goal:
            return reconstruct_path(came_from, current)
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(grid, *neighbor):
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    open_set.push(neighbor, f_score)
                    came_from[neighbor] = current
    return None

def gbfs(grid, start, goal):
    open_set = PriorityQueue()
    open_set.push(start, heuristic(start, goal))
    came_from = {}
    visited = set()
    while not open_set.is_empty():
        current = open_set.pop()
        if current == goal:
            return reconstruct_path(came_from, current)
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(grid, *neighbor) and neighbor not in visited:
                open_set.push(neighbor, heuristic(neighbor, goal))
                if neighbor not in came_from:
                    came_from[neighbor] = current
    return None

def get_grid_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    grid = []
    print("Enter the grid values (0 for open, 1 for obstacle):")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for cell ({i}, {j}): "))
            row.append(value)
        grid.append(row)
    return grid

def get_start_goal_input(grid):
    start_x = int(input("Enter the start x coordinate: "))
    start_y = int(input("Enter the start y coordinate: "))
    goal_x = int(input("Enter the goal x coordinate: "))
    goal_y = int(input("Enter the goal y coordinate: "))
    
    if not (0 <= start_x < len(grid) and 0 <= start_y < len(grid[0])):
        raise ValueError("Start coordinates are out of bounds.")
    if not (0 <= goal_x < len(grid) and 0 <= goal_y < len(grid[0])):
        raise ValueError("Goal coordinates are out of bounds.")
    
    return (start_x, start_y), (goal_x, goal_y)

if __name__ == '__main__':
    grid = get_grid_input()
    start, goal = get_start_goal_input(grid)

    path_astar = a_star(grid, start, goal)
    print("A* Path:" if path_astar else "No A* path found")
    if path_astar: 
        print(path_astar)

    path_gbfs = gbfs(grid, start, goal)
    print("GBFS Path:" if path_gbfs else "No GBFS path found")
    if path_gbfs: 
        print(path_gbfs)


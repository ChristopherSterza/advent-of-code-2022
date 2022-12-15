from pathlib import Path
from string import ascii_lowercase


def getInput(path: str) -> list[str]:
    input = Path(path).read_text().splitlines()
    return input


def find_S_and_E(terrain: dict, rows: int, cols: int) -> list[tuple()]:
    start = end = (-1, -1)
    for row in range(rows):
        for col in range(cols):
            if terrain[(row, col)] == "S":
                start = (row, col)
            if terrain[(row, col)] == "E":
                end = (row, col)
    return [start, end]


def init_visited_dict(rows: int, cols: int) -> dict:
    visited = {}
    for i in range(rows):
        for j in range(cols):
            visited[(i, j)] = False
    return visited


def init_terrain_dict(input: list[str]) -> dict:
    terrain = {}
    for row, line in enumerate(input):
        for col, char in enumerate(line):
            terrain[(row, col)] = char
    return terrain


def BFS(
    terrain: dict,
    visited: dict,
    parent: dict,
    start: tuple,
    reversed: bool,
    rows: int,
    cols: int,
):
    height = dict(zip(ascii_lowercase, range(1, 27)))
    height["S"], height["E"] = 1, 26
    queue = [start]
    visited[start] = True
    parent[start] = None

    while queue:
        pos = queue.pop(0)
        adj = [
            (pos[0] - 1, pos[1]),  # Up
            (pos[0] + 1, pos[1]),  # Down
            (pos[0], pos[1] - 1),  # Left
            (pos[0], pos[1] + 1),  # Right
        ]
        # Within row bounds
        adj = list(filter(lambda route: 0 <= route[0] < rows, adj))
        # Within col bounds
        adj = list(filter(lambda route: 0 <= route[1] < cols, adj))
        # Not already visited
        adj = list(filter(lambda route: not visited[route], adj))
        # Within height bounds
        if reversed:
            adj = list(
                filter(
                    lambda route: height[terrain[route]] >= height[terrain[pos]] - 1,
                    adj,
                )
            )
        else:
            adj = list(
                filter(
                    lambda route: height[terrain[route]] <= height[terrain[pos]] + 1,
                    adj,
                )
            )
        for route in adj:
            queue.append(route)
            visited[route] = True
            parent[route] = pos

    return


def find_path(parent: dict, destination: tuple) -> list[tuple]:
    path = [destination]
    pos = parent[destination]
    while pos != None:
        path = [pos] + path
        pos = parent[pos]
    return path


def part1(input: list[str]) -> str:
    rows, cols = len(input), len(input[0])
    terrain = init_terrain_dict(input)
    visited = init_visited_dict(rows, cols)
    start, end = find_S_and_E(terrain, rows, cols)
    parent = {}

    BFS(terrain, visited, parent, start, False, rows, cols)
    path = find_path(parent, end)
    return str(len(path) - 1)


def part2(input: list[str]) -> str:
    rows, cols = len(input), len(input[0])
    terrain = init_terrain_dict(input)
    visited = init_visited_dict(rows, cols)
    start, end = find_S_and_E(terrain, rows, cols)
    parent = {}

    # Get parents for all "a's" connected to the end
    BFS(terrain, visited, parent, end, True, rows, cols)
    shortest = rows * cols  # All paths shorter than visiting each cell
    for row in range(rows):
        for col in range(cols):
            if terrain[(row, col)] in ["S", "a"] and (row, col) in parent:
                path = find_path(parent, (row, col))
                shortest = min(shortest, len(find_path(parent, (row, col))) - 1)

    return str(shortest)


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

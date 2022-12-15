from pathlib import Path


class Node:
    def __init__(self, row=-1, col=-1, height=-1, parent=None) -> None:
        self.row = row
        self.col = col
        self.height = height
        self.parent = parent
        self.visited = False


def getInput(path: str) -> list[str]:
    input = Path(path).read_text().splitlines()
    return input


def init_grid(input: list[list[str]]):
    rows, cols = len(input), len(input[0])
    grid = [[Node for col in range(cols)] for row in range(rows)]
    for row, line in enumerate(input):
        for col, char in enumerate(line):
            grid[row][col] = Node(row, col, ord(char))
            if ord(char) == ord("S"):
                start = grid[row][col]
                start.height = ord("a")
            if ord(char) == ord("E"):
                end = grid[row][col]
                end.height = ord("z")
    return {"grid": grid, "start": start, "end": end}


def get_path(destination: Node) -> list[Node]:
    path = [destination]
    curr_node = destination
    while curr_node.parent != None:
        path = [curr_node.parent] + path
        curr_node = curr_node.parent
    return path


# Rearranges all the nodes into a BFS parent-tree
def BFS(reversed: bool, source: Node, grid: list[list[Node]]):
    source.parent = None
    queue = [source]
    source.visited = True
    rows, cols = len(grid), len(grid[0])

    while queue:
        node = queue.pop(0)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = node.row + dx, node.col + dy
            if x < 0 or x >= rows or y < 0 or y >= cols:  # Check grid bounds
                continue
            if reversed and grid[x][y].height < node.height - 1:  # Check height
                continue
            elif not reversed and grid[x][y].height > node.height + 1:
                continue
            next_node = grid[x][y]
            if next_node.visited:  # Check if node was already visited
                continue
            next_node.parent = node
            queue.append(next_node)
            next_node.visited = True


def part1(input: list[str]) -> str:
    values = init_grid(input)
    grid, start, end = values["grid"], values["start"], values["end"]

    BFS(reversed=False, source=start, grid=grid)
    return str(len(get_path(destination=end)) - 1)


def part2(input: list[str]) -> str:
    values = init_grid(input)
    grid, end = values["grid"], values["end"]
    rows, cols = len(grid), len(grid[0])

    BFS(reversed=True, source=end, grid=grid)
    shortest = rows * cols  # All paths shorter than visiting each node
    for row in grid:
        for node in row:
            if node.visited and node.height == ord("a"):
                shortest = min(shortest, len(get_path(node)) - 1)
    return str(shortest)


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

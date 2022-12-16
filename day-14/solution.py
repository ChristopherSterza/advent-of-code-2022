from pathlib import Path


class Point:
    def __init__(self, x=0, y=0, content=" ") -> None:
        self.x = x
        self.y = y
        self.content = content


def getInput(path: str) -> list[str]:
    input = Path(path).read_text().splitlines()
    return input


def print_scene(occupied: dict):
    x_min, y_min = x_max, y_max = list(occupied)[0]
    for point in occupied:
        x_min = min(x_min, point[0])
        x_max = max(x_max, point[0])
        y_min = min(y_min, point[1])
        y_max = max(y_max, point[1])
    for y in range(y_min, y_max + 1):
        print(y, end="|")
        for x in range(x_min, x_max + 1):
            if (x, y) in occupied:
                print(occupied[(x, y)].content, end="")
            else:
                print(" ", end="")
        print("")


def parse_walls(input: list[str]) -> dict:
    occupied = {}
    for line in input:
        points = [tuple(map(int, point.split(","))) for point in line.split(" -> ")]
        old_point = points[0]
        for new_point in points:
            x_dir = 1 if old_point[0] <= new_point[0] else -1
            y_dir = 1 if old_point[1] <= new_point[1] else -1
            for x in range(old_point[0], new_point[0] + x_dir, x_dir):
                occupied[(x, new_point[1])] = Point(x, new_point[1], "#")
            for y in range(old_point[1], new_point[1] + y_dir, y_dir):
                occupied[(new_point[0], y)] = Point(new_point[0], y, "#")
            old_point = new_point
    return occupied


def fill_sand1(occupied: dict):
    y_max = list(occupied)[0][1]
    for point in occupied:
        y_max = max(y_max, point[1])
    source = (500, 0)
    done = False
    while not done:
        grain = Point(source[0], source[1], ".")
        settled = False
        while not settled:
            settled = True
            if grain.y + 1 > y_max:
                done = True
            elif (grain.x, grain.y + 1) not in occupied:
                grain.y += 1
                settled = False
            elif (grain.x - 1, grain.y + 1) not in occupied:
                grain.x -= 1
                grain.y += 1
                settled = False
            elif (grain.x + 1, grain.y + 1) not in occupied:
                grain.x += 1
                grain.y += 1
                settled = False
        if not done:
            occupied[(grain.x, grain.y)] = grain
    return


def fill_sand2(occupied: dict):
    y_max = list(occupied)[0][1]
    for point in occupied:
        y_max = max(y_max, point[1])
    source = (500, 0)
    while source not in occupied:
        grain = Point(source[0], source[1], ".")
        settled = False
        while not settled:
            settled = True
            if grain.y + 1 == y_max + 2:
                settled = True
            elif (grain.x, grain.y + 1) not in occupied:
                grain.y += 1
                settled = False
            elif (grain.x - 1, grain.y + 1) not in occupied:
                grain.x -= 1
                grain.y += 1
                settled = False
            elif (grain.x + 1, grain.y + 1) not in occupied:
                grain.x += 1
                grain.y += 1
                settled = False
        occupied[(grain.x, grain.y)] = grain
    return


def part1(input: list[str]) -> str:
    occupied = parse_walls(input)
    fill_sand1(occupied)
    count = 0
    for point in occupied:
        if occupied[point].content == ".":
            count += 1
    return count


def part2(input: list[str]) -> str:
    occupied = parse_walls(input)
    fill_sand2(occupied)
    count = 0
    for point in occupied:
        if occupied[point].content == ".":
            count += 1
    return count


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

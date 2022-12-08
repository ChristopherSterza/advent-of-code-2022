from pathlib import Path
from collections import defaultdict


def getInput(path):
    input = Path(path).read_text().splitlines()
    return input


def getDirSizes(input) -> dict:
    path = Path()
    dir_size = defaultdict(int)
    for line in input:
        match line.split():
            case ["$", "cd", ".."]:
                path = path.parent
            case ["$", "cd", dir]:
                path = path / dir
            case ["$", "ls"]:
                continue
            case ["dir", dirname]:
                continue
            case [size, filename]:
                dir_size[path] += int(size)
                for dir in path.parents:
                    dir_size[dir] += int(size)
            case _:
                continue
    return dir_size


def part1(input):
    total = 0
    dir_size = getDirSizes(input)

    for size in dir_size.values():
        if size <= 100_000:
            total += size
    return total


def part2(input):
    dir_size = getDirSizes(input)
    disk_space = 70_000_000
    space_needed = 30_000_000
    space_used = max(dir_size.values())  # '/' should be the max value

    for size in sorted(dir_size.values()):
        if disk_space - space_used + size >= space_needed:
            return size

    return -1


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

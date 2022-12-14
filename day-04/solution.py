import pathlib
import re


def getInput(path):
    input = pathlib.Path(path).read_text().splitlines()
    return input


def part1(input):
    overlaps = 0
    for pair in input:
        a, b, x, y = map(int, re.findall(r"(\d+)", pair))
        if (a <= x and b >= y) or (a >= x and b <= y):
            overlaps += 1
    return overlaps


def part2(input):
    overlaps = 0
    for pair in input:
        a, b, x, y = map(int, re.findall(r"(\d+)", pair))
        if (a <= x <= b) or (x <= a <= y):
            overlaps += 1
    return overlaps


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

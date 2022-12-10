from pathlib import Path
from operator import sub


def getInput(path: str) -> list[str]:
    input = Path(path).read_text().splitlines()
    return input


def clamp(list: list, min_val: int, max_val: int):
    for i, el in enumerate(list):
        list[i] = max(min(el, max_val), min_val)


def step(rope: list[list[int, int]], direction: str) -> None:
    # Move head
    match direction:
        case "U":
            rope[0][0] += 1
        case "D":
            rope[0][0] -= 1
        case "L":
            rope[0][1] -= 1
        case "R":
            rope[0][1] += 1
    # Check if rest of rope segments need moving
    for segment in range(1, len(rope)):
        prev_seg = rope[segment - 1]
        # Get the distance from the previous rope segment
        distance = list(map(sub, prev_seg, rope[segment]))
        # Check if previous segment is too far
        if abs(distance[0]) >= 2 or abs(distance[1]) >= 2:
            # Clamp to get distance to move rope segment
            clamp(distance, -1, 1)
            rope[segment][0] += distance[0]
            rope[segment][1] += distance[1]
        else:
            break


def part1(input: list[str]) -> str:
    visited = set()
    rope = [[0, 0], [0, 0]]

    for instr in input:
        direction, steps = instr.split()
        for i in range(int(steps)):
            step(rope, direction)
            visited.add(tuple(rope[-1]))

    return str(len(visited))


def part2(input: list[str]) -> str:
    visited = set()
    rope_segments = 10
    rope = [[0, 0] for i in range(rope_segments)]

    for instr in input:
        direction, steps = instr.split()
        for i in range(int(steps)):
            step(rope, direction)
            visited.add(tuple(rope[-1]))

    return str(len(visited))


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

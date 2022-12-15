from pathlib import Path
from functools import cmp_to_key


def getInput(path: str) -> list[str]:
    input = Path(path).read_text().replace("\n\n", "\n").splitlines()
    return input


def compare(left, right) -> int:
    result = 0
    # Turn items into lists if they aren't already
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]

    # Iterate through items, recursively calling compare if an item is a list
    for i in range(min(len(left), len(right))):
        # Check if either item is a list
        if isinstance(left[i], list) or isinstance(right[i], list):
            result = compare(left[i], right[i])
            if result != 0:
                return result
        # current items are not lists, compare them
        elif left[i] < right[i]:
            return -1
        elif left[i] > right[i]:
            return 1
    # Iterated through all items in one or both lists. Compare lengths
    if len(left) < len(right):
        return -1
    if len(left) > len(right):
        return 1
    return 0  # Lists are identical


def part1(input: list[str]) -> str:
    input = list(map(eval, input))
    pairs = [input[i : i + 2] for i in range(0, len(input), 2)]
    total = 0
    for idx, pair in enumerate(pairs, 1):
        result = compare(pair[0], pair[1])
        if result <= 0:
            total += idx

    return str(total)


def part2(input: list[str]) -> str:
    input = list(map(eval, input))
    input.extend([[[2]], [[6]]])
    input = sorted(input, key=cmp_to_key(compare))
    idx1, idx2 = input.index([[2]]) + 1, input.index([[6]]) + 1
    return str(idx1 * idx2)


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

from pathlib import Path


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


def quick_sort(input: list[str], low: int, high: int):
    if low < high:
        part_idx = partition(input, low, high)
        quick_sort(input, low, part_idx - 1)
        quick_sort(input, part_idx + 1, high)
    return


def partition(input: list[str], low: int, high: int) -> int:
    pivot = input[high]
    i = low - 1

    for j in range(low, high + 1):
        if compare(eval(input[j]), eval(pivot)) < 0:
            i += 1
            input[i], input[j] = input[j], input[i]
    input[i + 1], input[high] = input[high], input[i + 1]
    return i + 1


def part1(input: list[str]) -> str:
    pairs = [input[i : i + 2] for i in range(0, len(input), 2)]
    total = 0
    for idx, pair in enumerate(pairs, 1):
        result = compare(eval(pair[0]), eval(pair[1]))
        if result <= 0:
            total += idx

    return str(total)


def part2(input: list[str]) -> str:
    input = ["[[2]]", "[[6]]"] + input
    quick_sort(input, 0, len(input) - 1)
    idx2, idx6 = input.index("[[2]]") + 1, input.index("[[6]]") + 1
    return str(idx2 * idx6)


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

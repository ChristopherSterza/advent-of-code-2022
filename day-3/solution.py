import pathlib
import string


def getInput(path):
    input = pathlib.Path(path).read_text().splitlines()
    return input


def part1(input):
    priorities = dict(zip(string.ascii_letters, range(1, 53)))
    total = 0

    for sack in input:
        checklist = set()
        endSack = len(sack)
        halfSack = int(endSack / 2)
        for i in range(0, halfSack):
            item = sack[i]
            checklist.add(item)
        for i in range(halfSack, endSack):
            item = sack[i]
            if item in checklist:
                total += priorities[item]
                break
    return total


def part2(input):
    return


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

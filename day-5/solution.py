import pathlib
import re
import copy

# Extra dummy list at index 0 to help with the instructions
stacks = [
    [],
    ["L", "N", "W", "T", "D"],
    ["C", "P", "H"],
    ["W", "P", "H", "N", "D", "G", "M", "J"],
    ["C", "W", "S", "N", "T", "Q", "L"],
    ["P", "H", "C", "N"],
    ["T", "H", "N", "D", "M", "W", "Q", "B"],
    ["M", "B", "R", "J", "G", "S", "L"],
    ["Z", "N", "W", "G", "V", "B", "R", "T"],
    ["W", "G", "D", "N", "P", "L"],
]

# Rewrite later to parse crate start state and also return instruction list. Not hardcoded
def getInput(path):
    input = pathlib.Path(path).read_text().splitlines()
    return input[10:]


def part1(input):
    res = ""
    tmpStacks = copy.deepcopy(stacks)
    for instr in input:
        count, fr, to = map(int, re.findall(r"(\d+)", instr))
        for i in range(count):
            tmpStacks[to].append(tmpStacks[fr].pop())
    for i in range(1, len(tmpStacks)):
        if tmpStacks[i]:
            res += tmpStacks[i][-1]
    return res


def part2(input):
    res = ""
    tmpStacks = copy.deepcopy(stacks)
    for instr in input:
        count, fr, to = map(int, re.findall(r"(\d+)", instr))
        tmpStacks[to].extend(tmpStacks[fr][-count:])
        del tmpStacks[fr][-count:]
    for i in range(1, len(stacks)):
        if tmpStacks[i]:
            res += tmpStacks[i][-1]
    return res


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

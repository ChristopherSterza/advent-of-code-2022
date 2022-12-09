from pathlib import Path


def getInput(path):
    input = Path(path).read_text().splitlines()
    return input


def part1(input):
    visited = set()
    ptr_head, ptr_tail = [0, 0], [0, 0]

    for instr in input:
        # print(instr)
        match instr.split():
            case ["U", qty]:
                for step in range(int(qty)):
                    ptr_head[0] += 1
                    if ptr_tail[0] + 1 < ptr_head[0]:
                        ptr_tail[0] += 1
                        ptr_tail[1] = ptr_head[1]
                    visited.add(tuple(ptr_tail))
            case ["D", qty]:
                for step in range(int(qty)):
                    ptr_head[0] -= 1
                    if ptr_tail[0] - 1 > ptr_head[0]:
                        ptr_tail[0] -= 1
                        ptr_tail[1] = ptr_head[1]
                    visited.add(tuple(ptr_tail))
            case ["L", qty]:
                for step in range(int(qty)):
                    ptr_head[1] -= 1
                    if ptr_tail[1] - 1 > ptr_head[1]:
                        ptr_tail[1] -= 1
                        ptr_tail[0] = ptr_head[0]
                    visited.add(tuple(ptr_tail))
            case ["R", qty]:
                for step in range(int(qty)):
                    ptr_head[1] += 1
                    if ptr_tail[1] + 1 < ptr_head[1]:
                        ptr_tail[1] += 1
                        ptr_tail[0] = ptr_head[0]
                    visited.add(tuple(ptr_tail))
            case _:
                continue

    return len(visited)


def part2(input):
    return


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

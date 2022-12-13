from pathlib import Path


def getInput(path: str) -> list[str]:
    input = Path(path).read_text().splitlines()
    return input


def printScreen(screen: list[str], return_str: str) -> str:
    return_str += "\n=======================================\n"
    for i in range(6):
        for j in range(40):
            return_str += screen[i * 40 + j]
        return_str += "\n"
    return_str += "======================================="
    return return_str


def drawToScreen(screen: list[str], sprite_pos: int, cycle: int):
    if cycle % 40 in [sprite_pos - 1, sprite_pos, sprite_pos + 1]:
        screen[cycle] = "#"


def part1(input: list[str]) -> str:
    register = 1
    cycle = 0
    checkpoint = 20
    total = 0

    for line in input:
        instr = line.split()
        cycle += 1
        if instr[0] == "noop":
            continue

        cycle += 1
        if cycle >= checkpoint:
            total += register * checkpoint
            checkpoint += 40
        register += int(instr[1])

    return total


def part2(input: list[str]) -> str:
    pixel_count = 240
    screen = [" " for pixel in range(pixel_count)]
    register = 1
    cycle = 0
    return_str = ""

    for line in input:
        drawToScreen(screen, register, cycle)
        instr = line.split()
        cycle += 1
        if instr[0] == "noop":
            continue
        drawToScreen(screen, register, cycle)
        cycle += 1
        register += int(instr[1])
    return_str = printScreen(screen, return_str)
    return return_str


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

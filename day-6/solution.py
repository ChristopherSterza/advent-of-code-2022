import pathlib


def getInput(path):
    input = pathlib.Path(path).read_text().splitlines()
    return input


def part1(input):
    signal = input[0]
    window_size = 4

    for i in range(window_size, len(signal) + 1):
        if len(set(signal[i - window_size : i])) == window_size:
            return i
    return -1


def part2(input):
    signal = input[0]
    window_size = 14

    for i in range(window_size, len(signal) + 1):
        if len(set(signal[i - window_size : i])) == window_size:
            return i
    return -1


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

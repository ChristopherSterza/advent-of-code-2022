import re
import sys


def main() -> None:
    file = open("input.txt", "r")
    data = file.readlines()

    t = 0
    for line in data:
        a, b, c, d = map(int, re.findall(r"(\d+)", line))
        if (a >= c and b <= d) or (c >= a and d <= b):
            t += 1

    print(t)


if __name__ == "__main__":
    main()

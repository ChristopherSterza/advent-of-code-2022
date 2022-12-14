from pathlib import Path
from collections import deque


class Monkey:
    inventory: deque[int]
    operation: str
    test: int
    if_true: int
    if_false: int
    items_inspected: int


def getInput(path: str) -> list[str]:
    input = Path(path).read_text().replace(",", "").split("\n\n")
    return input


def parseMonkeys(input: list[str]) -> list[Monkey]:
    monkeys = []
    for monkey_input in input:
        monkey_info = monkey_input.split("\n")

        monkey = Monkey()
        monkey.inventory = deque(map(int, monkey_info[1].split()[2:]))
        monkey.operation = monkey_info[2].split("= ")[1]
        monkey.test = int(monkey_info[3].split()[-1])
        monkey.if_true = int(monkey_info[4].split()[-1])
        monkey.if_false = int(monkey_info[5].split()[-1])
        monkey.items_inspected = 0
        monkeys.append(monkey)
    return monkeys


def simulateRounds(
    monkeys: list[Monkey] = [], rounds: int = 0, relief: int = 1, mod: int = 0
) -> int:
    for round in range(rounds):
        for monkey in monkeys:
            while len(monkey.inventory) > 0:
                item = monkey.inventory.popleft()
                monkey.items_inspected += 1
                item = eval(monkey.operation, {"old": item}) // relief
                # Keep the int from growing too large
                if mod:
                    item %= mod
                if item % monkey.test == 0:
                    monkeys[monkey.if_true].inventory.append(item)
                else:
                    monkeys[monkey.if_false].inventory.append(item)
    monkey_activity = sorted(
        [monkey.items_inspected for monkey in monkeys], reverse=True
    )
    return monkey_activity[0] * monkey_activity[1]


def part1(input: list[str]) -> str:
    monkeys = parseMonkeys(input)
    return simulateRounds(monkeys, 20, 3)


def part2(input: list[str]) -> str:
    monkeys = parseMonkeys(input)
    # Need the modulus to keep the worry level down (otherwise it slows code and causes errors). Needs to be a common multiple of all monkeys as to not affect divisibility
    mod = 1
    for monkey in monkeys:
        mod *= monkey.test
    return simulateRounds(monkeys, 10000, 1, mod)


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

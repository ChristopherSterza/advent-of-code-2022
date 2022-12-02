import pathlib


def getInput(path):
  input = pathlib.Path(path).read_text().splitlines()
  return input


# Assuming X,Y,Z are rock, paper, scissors
def part1(input):
  score = 0
  choiceMap = {"X": 1, "Y": 2, "Z": 3}
  resultMap = {
      "AX": 3,
      "AY": 6,
      "AZ": 0,
      "BX": 0,
      "BY": 3,
      "BZ": 6,
      "CX": 6,
      "CY": 0,
      "CZ": 3,
  }
  for game in input:
    theirChoice, myChoice = game.split()
    score += choiceMap[myChoice] + resultMap[theirChoice + myChoice]
  return score


# Assuming X,Y,Z are lose, tie, win
def part2(input):
  score = 0
  choiceMap = {"X": 0, "Y": 3, "Z": 6}
  resultMap = {
      "AX": 3,
      "AY": 1,
      "AZ": 2,
      "BX": 1,
      "BY": 2,
      "BZ": 3,
      "CX": 2,
      "CY": 3,
      "CZ": 1,
  }

  for game in input:
    theirChoice, myChoice = game.split()
    score += choiceMap[myChoice] + resultMap[theirChoice + myChoice]
  return score


def main():
  input = getInput("input.txt")
  print(f'Answer to part 1: {part1(input)}')
  print(f'Answer to part 2: {part2(input)}')
  return


if __name__ == "__main__":
  main()

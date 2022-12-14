import pathlib

def getInput(path):
  input = pathlib.Path(path).read_text().splitlines()
  return input

def part1(input):
  calorieTotal = []
  elfCalorieTotal = 0

  for line in input:
    if line:
      elfCalorieTotal += int(line)
    else:
      calorieTotal.append(elfCalorieTotal)
      elfCalorieTotal = 0
  
  return max(calorieTotal)

def part2(input):
  calorieTotal = []
  elfCalorieTotal = 0

  for line in input:
    if line:
      elfCalorieTotal += int(line)
    else:
      calorieTotal.append(elfCalorieTotal)
      elfCalorieTotal = 0
  
  calorieTotal.sort()
  return sum(calorieTotal[-3:])

def main():
  input = getInput('input.txt')
  print(f'Answer to part 1: {part1(input)}')
  print(f'Answer to part 2: {part2(input)}')
  return

if __name__ == "__main__":
    main()
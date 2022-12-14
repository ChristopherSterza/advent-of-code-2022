from pathlib import Path
from math import prod


def getInput(path):
    input = Path(path).read_text().splitlines()
    return input


def getTreeMatrix(input) -> list[list[int]]:
    tree_matrix = []
    for row in input:
        # Unpack and int convert each element in the row and append it to the matrix
        tree_matrix.append([int(i) for i in [*row]])
    return tree_matrix


def part1(input):
    tree_matrix = getTreeMatrix(input)
    mat_hgt = len(tree_matrix)
    mat_wth = len(tree_matrix[0])
    visibility_matrix = [[0 for x in range(mat_wth)] for y in range(mat_hgt)]

    # Find which trees are visible from west or east
    for i in range(mat_hgt):
        max_height = -1
        for j in range(mat_wth):
            if tree_matrix[i][j] > max_height:
                max_height = tree_matrix[i][j]
                visibility_matrix[i][j] = 1
        max_height = -1
        for j in range(mat_wth - 1, -1, -1):
            if tree_matrix[i][j] > max_height:
                max_height = tree_matrix[i][j]
                visibility_matrix[i][j] = 1

    # Find which trees are visible from north and south
    for j in range(mat_wth):
        max_height = -1
        for i in range(mat_hgt):
            if tree_matrix[i][j] > max_height:
                max_height = tree_matrix[i][j]
                visibility_matrix[i][j] = 1
        max_height = -1
        for i in range(mat_hgt - 1, -1, -1):
            if tree_matrix[i][j] > max_height:
                max_height = tree_matrix[i][j]
                visibility_matrix[i][j] = 1

    return sum(sum(row) for row in visibility_matrix)


def part2(input):
    tree_matrix = getTreeMatrix(input)
    mat_hgt = len(tree_matrix)
    mat_wth = len(tree_matrix[0])
    max_score = 0

    for i in range(mat_hgt):
        for j in range(mat_wth):
            # For all trees, check view dist in all directions
            tree_height = tree_matrix[i][j]
            view_dist = [0, 0, 0, 0]
            for k in range(i - 1, -1, -1):  # Check the north
                view_dist[0] += 1
                if tree_matrix[k][j] >= tree_height:
                    break
            for k in range(j - 1, -1, -1):  # Check the west
                view_dist[1] += 1
                if tree_matrix[i][k] >= tree_height:
                    break
            for k in range(i + 1, mat_hgt):  # Check the south
                view_dist[2] += 1
                if tree_matrix[k][j] >= tree_height:
                    break
            for k in range(j + 1, mat_wth):  # Check the east
                view_dist[3] += 1
                if tree_matrix[i][k] >= tree_height:
                    break
            max_score = max(max_score, prod(view_dist))

    return max_score


def main():
    input = getInput("input.txt")
    print(f"Answer to part 1: {part1(input)}")
    print(f"Answer to part 2: {part2(input)}")
    return


if __name__ == "__main__":
    main()

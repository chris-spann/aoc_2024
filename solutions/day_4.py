from utils.input_utils import get_input


def is_valid_coordinate(x: int, y: int, matrix: list[str]) -> bool:
    return bool(x < len(matrix) and x >= 0 and y < len(matrix[0]) and y >= 0)


def get_directions(x: int, y: int, search_str: str, matrix: list[str]):
    # return a list of each releative coords to the current position
    length = len(search_str)
    directions = {
        "up": [],
        "down": [],
        "left": [],
        "right": [],
        "up_right": [],
        "up_left": [],
        "down_right": [],
        "down_left": [],
    }
    for i in range(length):
        if is_valid_coordinate(x, y + i, matrix):
            directions["right"].append(matrix[x][y + i])
        else:
            directions["right"].append("R")

        if is_valid_coordinate(x, y - i, matrix):
            directions["left"].append(matrix[x][y - i])
        else:
            directions["left"].append("R")

        if is_valid_coordinate(x - i, y, matrix):
            directions["up"].append(matrix[x - i][y])
        else:
            directions["up"].append("R")

        if is_valid_coordinate(x + i, y, matrix):
            directions["down"].append(matrix[x + i][y])
        else:
            directions["down"].append("R")

        if is_valid_coordinate(x + i, y + i, matrix):
            directions["down_right"].append(matrix[x + i][y + i])
        else:
            directions["down_right"].append("R")

        if is_valid_coordinate(x - i, y + i, matrix):
            directions["up_right"].append(matrix[x - i][y + i])
        else:
            directions["up_right"].append("R")

        if is_valid_coordinate(x + i, y - i, matrix):
            directions["down_left"].append(matrix[x + i][y - i])
        else:
            directions["down_left"].append("R")

        if is_valid_coordinate(x - i, y - i, matrix):
            directions["up_left"].append(matrix[x - i][y - i])
        else:
            directions["up_left"].append("R")
    return directions


def part_1(lines: list[str]):
    total = 0
    search_str = "XMAS"
    matrix = [line.strip() for line in lines]
    dirs = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            directions = get_directions(i, j, search_str, matrix)
            dirs.append({"coords": (i, j), "directions": directions})
            for direction in directions.values():
                if search_str in "".join(direction):
                    total += 1
    print(total)
    return total


def part_2(lines: list[str]):
    total = 0
    search_str = "MAS"
    search_strings = ["MAS", "SAM"]
    matrix = [line.strip() for line in lines]
    dirs = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            directions = get_directions(i, j, search_str, matrix)
            second = get_directions(i + 2, j, search_str, matrix)
            dirs.append({"coords": (i, j), "directions": directions})
            if (
                "".join(directions["down_right"]) in search_strings
                and "".join(second["up_right"]) in search_strings
            ):
                total += 1

    print(total)
    return total


def main():
    lines = get_input(__file__)
    part_1(lines)
    part_2(lines)


if __name__ == "__main__":  # pragma: no cover
    main()

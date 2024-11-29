from utils.input_utils import get_input


def sum_calibration_values(lines: list[str]):
    sum = 0
    for line in lines:
        ints = ""
        for item in line:
            if item.isnumeric():
                ints += item
        sum += int("".join([ints[0], ints[-1]]))
    print(sum)
    return sum


def sum_calibration_values2(lines: list[str]):
    sum = 0
    d = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for line in lines:
        ints = ""
        for i, j in enumerate(line):
            if j.isnumeric():
                ints += j
            else:
                for key, value in d.items():
                    if line[i:].startswith(key):
                        ints += str(value)
        sum += int("".join([ints[0], ints[-1]]))
    print(sum)
    return sum


def main():
    lines = get_input(__file__)
    sum_calibration_values(lines)
    sum_calibration_values2(lines)


if __name__ == "__main__":  # pragma: no cover
    main()

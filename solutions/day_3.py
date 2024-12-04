import re

from utils.input_utils import get_input


def part_1(lines: list[str]):
    total = 0
    for line in lines:
        muls = re.findall(r"mul\(\d+,\d+\)", line)
        for mul in muls:
            matches = re.findall(r"\d+", mul)
            if len(matches) == 2:
                x = int(matches[0]) * int(matches[1])
                total += x
    print(total)
    return total


def part_2(lines: list[str]) -> int:
    total = 0
    pattern = r"do\(\)|mul\(\d+,\d+\)|don't\(\)"
    line = "".join(lines)
    use = True
    matches = re.findall(pattern, line)

    for item in matches:
        if item == "do()":
            use = True
        elif item == "don't()":
            use = False
        elif "mul" in item and use:
            mat = re.findall(r"\d+", item)
            if len(mat) == 2:
                total += int(mat[0]) * int(mat[1])
    print(total)
    return total


def main():
    lines = get_input(__file__)
    part_1(lines)
    part_2(lines)


if __name__ == "__main__":  # pragma: no cover
    main()

from utils.input_utils import get_input


def get_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    left = []
    right = []
    for line in lines:
        a, b = line.split("   ")
        left.append(int(a.strip()))
        right.append(int(b.strip()))
    return left, right


def part_1(lines: list[str]) -> int:
    sum = 0
    left, right = get_lists(lines)
    left.sort()
    right.sort()
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
    print(sum)
    return sum


def part_2(lines: list[str]):
    print(lines)
    return lines


#     sum = 0
#     left, right = get_lists(lines)
#     for i in left:
#         sum += right.count(i) * i
#     print(sum)
#     return sum


def main():
    lines = get_input(__file__)
    part_1(lines)
    # part_2(lines)


if __name__ == "__main__":  # pragma: no cover
    main()

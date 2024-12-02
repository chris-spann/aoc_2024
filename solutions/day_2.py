from utils.input_utils import get_input


def part_1(lines: list[str]):
    save_report_count = 0
    for line in lines:
        diffs = []
        items = line.split(" ")
        for i in range(len(items) - 1):
            diffs.append(int(items[i + 1]) - int(items[i]))

        all_positive = all(d > 0 for d in diffs)
        all_negative = all(d < 0 for d in diffs)
        if (all_positive or all_negative) and (max(diffs) <= 3 and min(diffs) >= -3):
            save_report_count += 1
    return save_report_count


def part_2(lines: list[str]):
    print(lines)
    return lines


def main():
    lines = get_input(__file__)
    part_1(lines)
    # part_2(lines)


if __name__ == "__main__":  # pragma: no cover
    main()

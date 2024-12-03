from utils.input_utils import get_input


# Get all sublists of a list by just removing one item
# [1,2,3,4] -> [[2,3,4], [1,3,4], [1,2,4], [1,2,3]]
def list_subs(lst: list[int]) -> list[list[int]]:
    return [lst[:i] + lst[i+1:] for i in range(len(lst))]

def is_safe_diffs(diffs: list[int]) -> bool:
    all_positive = all(d > 0 for d in diffs)
    all_negative = all(d < 0 for d in diffs)
    return (all_positive or all_negative) and (max(diffs) <= 3 and min(diffs) >= -3)

def part_1(lines: list[str]):
    safe_report_count = 0
    for line in lines:
        diffs = []
        items = line.split(" ")
        for i in range(len(items) - 1):
            diffs.append(int(items[i + 1]) - int(items[i]))
        if is_safe_diffs(diffs):
            safe_report_count += 1
    print(safe_report_count)
    return safe_report_count
    

def part_2(lines: list[str]):
    safe_report_count = 0
    unsafe_report_list = []

    for line in lines:
        diffs = []
        items = line.split(" ")
        for i in range(len(items) - 1):
            diffs.append(int(items[i + 1]) - int(items[i]))
        
        if is_safe_diffs(diffs):
            safe_report_count += 1
        else:
            unsafe_report_list.append(line)
    # print(f"Initial safe report: {save_report_count}")
    # print(f"checking unsafe list: {unsafe_report_list}")
    
    for unsafe_report in unsafe_report_list:
        items = unsafe_report.split(" ")
        items = [int(i) for i in items]
        subs = list_subs(items)
        for s in subs:
            unsafe_diffs = []
            for i in range(len(s) - 1):
                unsafe_diffs.append(s[i + 1] - s[i])
            if is_safe_diffs(unsafe_diffs):
                safe_report_count += 1
                # print(f"sublist {s} is safe")
                break
            
    print(safe_report_count)
    return safe_report_count


def main():
    lines = get_input(__file__)
    part_1(lines)
    part_2(lines)


if __name__ == "__main__":  # pragma: no cover
    main()

from utils.input_utils import get_input


def part_1(lines: list[str]):
    total = 0
    rules = []
    updates = []
    rules_or_pages = True
    correct_order = []
    for line in lines:
        if rules_or_pages:
            if line == "\n":
                rules_or_pages = False
                continue
            rules.append(line.strip())
        else:
            updates.append(line.strip())
    big_pages = []
    for pages in updates:
        pages = pages.split(",")
        big_pages.append([int(x) for x in pages])
    for page in big_pages:
        rule_results = []
        for rule in rules:
            try:
                if page.index(int(rule.split("|")[0])) < page.index(int(rule.split("|")[1])):
                    rule_results.append(True)
                else:
                    rule_results.append(False)
            except ValueError:
                rule_results.append(True)
        if all(rule_results):
            correct_order.append(page)
    # print(f"Correct Order: {correct_order}")
    for page in correct_order:
        # middle index
        middle = len(page) // 2
        total += page[middle]
    print(total)
    return total


def part_2(lines: list[str]):
    total = 0
    rules = []
    updates = []
    rules_or_pages = True
    correct_order = []
    updated_oness = []

    for line in lines:
        if rules_or_pages:
            if line == "\n":
                rules_or_pages = False
                continue
            rules.append(line.strip())
        else:
            updates.append(line.strip())

    big_pages = []
    for pages in updates:
        pages = pages.split(",")
        big_pages.append([int(x) for x in pages])

    incorrect = []
    for page in big_pages:
        rule_results = []
        for rule in rules:
            try:
                if page.index(int(rule.split("|")[0])) < page.index(int(rule.split("|")[1])):
                    rule_results.append(True)
                else:
                    rule_results.append(False)
            except ValueError:
                rule_results.append(True)
        if not all(rule_results):
            incorrect.append(page)

    for page in incorrect:
        # print(f"Checking Page: {page}")
        all_correct = False
        while not all_correct:
            rule_results = []
            for rule in rules:
                try:
                    first_value_index = page.index(int(rule.split("|")[0]))
                    second_value_index = page.index(int(rule.split("|")[1]))
                    if first_value_index < second_value_index:
                        rule_results.append(True)
                        continue
                    else:
                        rule_results.append(False)
                        # print(f"rule broken: {rule}")
                        va = page.pop(first_value_index)
                        page.insert(second_value_index, va)
                        # print(f"Updated Page: {page}")
                        updated_oness.append(page)
                        all_correct = False
                        break  # Break the inner loop to recheck all rules after updating
                except ValueError:
                    rule_results.append(True)
                    continue
            if all(rule_results):
                all_correct = True
        correct_order.append(page)

    # print(f"Correct Order: {correct_order}")
    # print(f"updated_oness: {updated_oness}")
    # for page in updated_oness:
    for page in correct_order:
        # middle index
        middle = len(page) // 2
        total += page[middle]
    print(total)
    return total


def main():
    lines = get_input(__file__)
    part_1(lines)
    part_2(lines)


if __name__ == "__main__":  # pragma: no cover
    main()

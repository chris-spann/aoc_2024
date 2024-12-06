import pytest


@pytest.fixture
def day_1_test_input():
    return [
        "3   4\n",
        "4   3\n",
        "2   5\n",
        "1   3\n",
        "3   9\n",
        "3   3\n",
    ]


@pytest.fixture
def day_2_test_input():
    return [
        "7 6 4 2 1\n",
        "1 2 7 8 9\n",
        "9 7 6 2 1\n",
        "1 3 2 4 5\n",
        "8 6 4 4 1\n",
        "1 3 6 7 9\n",
    ]


@pytest.fixture
def day_3_test_input():
    return [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))\n",
    ]


@pytest.fixture
def day_3_test_input_part_2():
    return [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))\n",
    ]


@pytest.fixture
def day_4_test_input():
    return [
        "MMMSXXMASM\n",
        "MSAMXMSMSA\n",
        "AMXSXMAAMM\n",
        "MSAMASMSMX\n",
        "XMASAMXAMM\n",
        "XXAMMXXAMA\n",
        "SMSMSASXSS\n",
        "SAXAMASAAA\n",
        "MAMMMXMMMM\n",
        "MXMXAXMASX\n",
    ]

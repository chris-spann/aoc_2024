from io import StringIO

from solutions.day_1 import main, sum_calibration_values, sum_calibration_values2


def test_sum_calibration_values():
    assert sum_calibration_values(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142


def test_sum_calibration_values2():
    assert (
        sum_calibration_values2(
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ]
        )
        == 281
    )


def test_main(mocker):
    mock_input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    mocker.patch("solutions.day_1.get_input", return_value=mock_input)
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)

    main()

    output = mock_stdout.getvalue().splitlines()

    assert output[0] == "142"
    assert output[1] == "142"

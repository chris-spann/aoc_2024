from solutions.day_3 import main, part_1, part_2


def test_part_1(day_3_test_input):
    assert part_1(day_3_test_input) == 161


def test_part_2(day_3_test_input_part_2):
    assert part_2(day_3_test_input_part_2) == 48


def test_main(mocker, day_3_test_input, capfd):
    mocker.patch("solutions.day_3.get_input", return_value=day_3_test_input)

    main()

    captured = capfd.readouterr()
    output = captured.out.splitlines()
    output = [int(line) for line in output]

    assert output[0] == 161
    assert output[1] == 161

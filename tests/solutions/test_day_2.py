from solutions.day_2 import main, part_1, part_2


def test_part_1(day_2_test_input):
    assert part_1(day_2_test_input) == 2


def test_part_2(day_2_test_input):
    assert part_2(day_2_test_input) == 4


def test_main(mocker, day_2_test_input, capfd):
    mocker.patch("solutions.day_2.get_input", return_value=day_2_test_input)

    main()

    captured = capfd.readouterr()
    output = captured.out.splitlines()
    output = [int(line) for line in output]

    assert output[0] == 2
    assert output[1] == 4

from solutions.day_4 import main, part_1, part_2


def test_part_1(day_4_test_input):
    assert part_1(day_4_test_input) == 18


def test_part_2(day_4_test_input):
    assert part_2(day_4_test_input) == 9


def test_main(mocker, day_4_test_input, capfd):
    mocker.patch("solutions.day_4.get_input", return_value=day_4_test_input)

    main()

    captured = capfd.readouterr()
    output = captured.out.splitlines()
    output = [int(line) for line in output]

    assert output[0] == 18
    assert output[1] == 9

from solutions.day_1 import main, part_1, part_2


def test_part_1(day_1_test_input):
    assert (part_1(day_1_test_input)) == 11


def test_part_2(day_1_test_input):
    assert part_2(day_1_test_input) == 31


def test_main(mocker, day_1_test_input, capfd):
    mocker.patch("solutions.day_1.get_input", return_value=day_1_test_input)

    main()

    captured = capfd.readouterr()
    output = captured.out.splitlines()
    output = [int(line) for line in output]

    assert output[0] == 11
    assert output[1] == 31

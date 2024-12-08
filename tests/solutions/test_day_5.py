from solutions.day_5 import main, part_1, part_2


def test_part_1(day_5_test_input):
    assert part_1(day_5_test_input) == 143


def test_part_2(day_5_test_input):
    assert part_2(day_5_test_input) == 123


def test_main(mocker, capfd):
    mocker.patch("solutions.day_5.get_input", return_value=[])

    main()

    captured = capfd.readouterr()
    output = captured.out.splitlines()
    output = [int(line) for line in output]

    assert output[0] is not None
    assert output[1] is not None

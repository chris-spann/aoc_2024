from solutions.day_2 import main, part_1, part_2


def test_part_1(day_2_test_input):
    assert part_1(day_2_test_input) == 2


def test_part_2():
    assert part_2([]) is not None


def test_main(mocker):
    mocker.patch("solutions.day_2.get_input", return_value=[])
    mock_stdout = mocker.patch("sys.stdout")

    main()

    output = mock_stdout.getvalue().splitlines()

    assert output[0] is not None
    assert output[1] is not None

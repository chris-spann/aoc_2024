from solutions.solution_template import main, part_1, part_2


def test_part_1():
    assert part_1([]) is not None


def test_part_2():
    assert part_2([]) is not None


def test_main(mocker):
    mocker.patch("solutions.solution_template.get_input", return_value=[])
    mock_stdout = mocker.patch("sys.stdout")

    main()

    output = mock_stdout.getvalue().splitlines()

    assert output[0] is not None
    assert output[1] is not None

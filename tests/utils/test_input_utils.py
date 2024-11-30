import os
from unittest.mock import mock_open

from utils.input_utils import get_input, get_input_file_path, read_file


def test_read_file(mocker):
    mocker.patch("builtins.open", mock_open(read_data="line1\nline2\nline3\n"))
    result = read_file("dummy_path")
    assert result == ["line1\n", "line2\n", "line3\n"]


def test_get_input_file_path():
    script_path = "/path/to/script.py"
    expected_path = os.path.join("/path", "inputs", "input.txt")
    result = get_input_file_path(script_path)
    assert result == expected_path


def test_get_input(mocker):
    mocker.patch("builtins.open", mock_open(read_data="line1\nline2\nline3\n"))
    mocker.patch("utils.input_utils.get_input_file_path", return_value="dummy_path")
    result = get_input("dummy_script_path")
    assert result == ["line1\n", "line2\n", "line3\n"]

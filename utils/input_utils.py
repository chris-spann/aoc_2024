import os


def read_file(filepath: str) -> list[str]:
    with open(filepath) as f:
        return f.readlines()


def get_input_file_path(script_path: str, filename: str = "input.txt") -> str:
    dir_path = os.path.dirname(os.path.abspath(script_path))
    file_path = os.path.join(dir_path, filename)
    return file_path


def get_input(script_path: str, file="input.txt"):
    return read_file(get_input_file_path(script_path, file))

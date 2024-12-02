import os


def read_file(filepath: str) -> list[str]:
    with open(filepath) as f:
        return f.readlines()


def get_input_file_path(script_path: str, filename: str = "input.txt") -> str:
    dir_path = os.path.dirname(os.path.abspath(script_path))
    parent_dir_path = os.path.dirname(dir_path)
    file_path = os.path.join(parent_dir_path, "inputs", filename)
    return file_path


def get_input(script_path: str, file="day_1_input.txt"):
    return read_file(get_input_file_path(script_path, file))

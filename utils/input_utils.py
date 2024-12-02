import os
import re


def read_file(filepath: str) -> list[str]:
    with open(filepath) as f:
        return f.readlines()


def get_input_file_path(script_path: str, filename: str = "input.txt") -> str:
    dir_path = os.path.dirname(os.path.abspath(script_path))
    parent_dir_path = os.path.dirname(dir_path)
    file_path = os.path.join(parent_dir_path, "inputs", filename)
    return file_path


def get_input(script_path: str):
    current_file_name = os.path.basename(script_path)
    match = re.search(r"day_(\d+)\.py", current_file_name)
    if match:
        day = int(match.group(1))
    else:
        raise ValueError("Could not extract day number from file name")
    return read_file(get_input_file_path(script_path, f"day_{day}_input.txt"))

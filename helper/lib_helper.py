from pathlib import Path


def check_is_file_exist(file_path):
    my_file = Path(file_path)
    if my_file.is_file() and my_file.exists():
        return True
    else:
        raise Exception('File not found')

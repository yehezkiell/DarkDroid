import re
from pathlib import Path

HEX_REGEX = "^#([0-9A-F]{3}){1,2}$"


def check_is_file_exist(file_path):
    my_file = Path(file_path)
    if my_file.is_file() and my_file.exists():
        return True
    else:
        raise Exception('File not found')


def is_hex_valid_color(hex) -> bool:
    result = re.match(HEX_REGEX, hex)
    if result:
        return True
    else:
        return False

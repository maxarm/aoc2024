import regex
import utils

PATTERN = r"mul\(\d{1,3},\d{1,3}\)"

def get_mul_sum(read_test_data: bool) -> int:
    lines = utils.read_lines(3, read_test_data)
    data = "".join(lines)
    matches = regex.findall(PATTERN, data, overlapped=True)
    result = sum(mul(match) for match in matches)
    return result


def mul(mult: str) -> int:
    stripped = mult.lstrip("mul(").rstrip(")")
    x, y = [int(x) for x in stripped.split(",")]
    return x * y

def get_mul_sum_without_donts(read_test_data: bool) -> int:
    lines = utils.read_lines_of_b(3, read_test_data)
    data = "".join(lines)
    stripped, data = remove_next_dont_block(data)
    while stripped:
        stripped, data = remove_next_dont_block(data)

    matches = regex.findall(PATTERN, data, overlapped=True)
    result = sum(mul(match) for match in matches)
    return result


def remove_next_dont_block(data: str) -> tuple[bool, str|None]:
    dont_idx = data.find("don't()")
    if dont_idx == -1:
        return False, data

    do_idx = data.find("do()", dont_idx+8)
    if do_idx == -1:
        return True, ""

    stripped = data[:dont_idx] + data[do_idx+4:]
    return True, stripped

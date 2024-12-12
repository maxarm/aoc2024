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

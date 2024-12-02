import utils
from typing import List


def get_number_of_safe_reports(read_test_data: bool = False) -> int:
    lines = utils.read_data(2, read_test_data)
    result = 0
    for line in lines:
        nums = get_numbers_of_string(line)
        if is_increasing_safely(nums):
            print(f"{nums} is increasing safely")
            result += 1
        elif is_decreasing_safely(nums):
            print(f"{nums} is decreasing safely")
            result += 1

    return result


def get_numbers_of_string(line: str) -> List[int]:
    return [int(x) for x in line.split(" ")]


def is_increasing_safely(nums: List[int]) -> bool:
    return all([
        x < y and
        abs(x-y) > 0 and
        abs(x-y) < 4
        for x, y in zip(nums, nums[1:])
    ])


def is_decreasing_safely(nums: List[int]) -> bool:
    return all([
        x > y and
        abs(x-y) > 0 and
        abs(x-y) < 4
        for x, y in zip(nums, nums[1:])
    ])

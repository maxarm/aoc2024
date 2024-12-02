import utils
from typing import List


def get_number_of_safe_reports(tolerate_a_bad_level: bool, read_test_data: bool) -> int:
    lines = utils.read_data(2, read_test_data)
    result = 0
    for line in lines:
        nums = get_numbers_of_string(line)
        if (is_increasing_safely(nums, tolerate_a_bad_level) or
                is_decreasing_safely(nums, tolerate_a_bad_level)):
            result += 1

    return result


def get_numbers_of_string(line: str) -> List[int]:
    return [int(x) for x in line.split(" ")]


def is_increasing_safely(nums: List[int], tolerate_a_bad_level: bool) -> bool:
    if is_increasing_safely_strict(nums):
        print(f"{nums}: Increasing safely without removing any level.")
        return True

    if tolerate_a_bad_level and is_increasing_safely_tolerantly(nums):
        print(f"{nums}: Increasing safely by removing a level.")
        return True

    return False


def is_decreasing_safely(nums: List[int], tolerate_a_bad_level: bool) -> bool:
    if is_decreasing_safely_strict(nums):
        print(f"{nums}: Decreasing safely without removing any level.")
        return True

    if tolerate_a_bad_level and is_decreasing_safely_tolerantly(nums):
        print(f"{nums}: Decreasing safely by removing a level.")
        return True

    return False


def remove_a_list_element(nums: List[int], index: int) -> List[int]:
    return nums[:index] + nums[index+1:]


def is_increasing_safely_tolerantly(nums: List[int]) -> bool:
    for i in range(0, len(nums)):
        new_list = remove_a_list_element(nums, i)
        if is_increasing_safely_strict(new_list):
            return True
    return False


def is_decreasing_safely_tolerantly(nums: List[int]) -> bool:
    for i in range(0, len(nums)):
        new_list = remove_a_list_element(nums, i)
        if is_decreasing_safely_strict(new_list):
            return True
    return False


def is_increasing_safely_strict(nums: List[int]) -> bool:
    return all([
        x < y and
        abs(x-y) > 0 and
        abs(x-y) < 4
        for x, y in zip(nums, nums[1:])
    ])


def is_decreasing_safely_strict(nums: List[int]) -> bool:
    return all([
        x > y and
        abs(x-y) > 0 and
        abs(x-y) < 4
        for x, y in zip(nums, nums[1:])
    ])

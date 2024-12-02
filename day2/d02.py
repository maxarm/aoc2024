from typing import List
import utils


def get_number_of_safe_reports(tolerant: bool, read_test_data: bool) -> int:
    lines = utils.read_data(2, read_test_data)
    result = 0
    for line in lines:
        nums = [int(x) for x in line.split(" ")]
        if (is_increasing_safely(nums, tolerant) or is_decreasing_safely(nums, tolerant)):
            result += 1

    return result


def is_increasing_safely(nums: List[int], tolerant: bool) -> bool:
    if is_increasing_safely_strict(nums):
        print(f"{nums}: Increasing safely.")
        return True

    if tolerant and is_increasing_safely_tolerantly(nums):
        print(f"{nums}: Increasing safely by removing a level.")
        return True

    return False


def is_decreasing_safely(nums: List[int], tolerate_a_bad_level: bool) -> bool:
    if is_decreasing_safely_strict(nums):
        print(f"{nums}: Decreasing safely.")
        return True

    if tolerate_a_bad_level and is_decreasing_safely_tolerantly(nums):
        print(f"{nums}: Decreasing safely by removing a level.")
        return True

    return False


def remove_element(nums: List[int], index: int) -> List[int]:
    return nums[:index] + nums[index+1:]


def get_shortened_list(nums):
    return [remove_element(nums, i) for i in range(0, len(nums))]


def is_increasing_safely_tolerantly(nums: List[int]) -> bool:
    shortened_lists = get_shortened_list(nums)
    return any(is_increasing_safely_strict(x) for x in shortened_lists)


def is_decreasing_safely_tolerantly(nums: List[int]) -> bool:
    shortened_lists = get_shortened_list(nums)
    return any(is_decreasing_safely_strict(x) for x in shortened_lists)


def is_increasing_safely_strict(nums: List[int]) -> bool:
    return all(
        x < y and
        abs(x-y) > 0 and
        abs(x-y) < 4
        for x, y in zip(nums, nums[1:])
    )


def is_decreasing_safely_strict(nums: List[int]) -> bool:
    return all(
        x > y and
        abs(x-y) > 0 and
        abs(x-y) < 4
        for x, y in zip(nums, nums[1:])
    )

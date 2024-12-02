import utils
from typing import List

def get_number_of_safe_reports(read_test_data: bool=False) -> int:
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
    str_nums = line.split(" ")
    nums = [int(x) for x in str_nums]
    return nums
    
def is_increasing_safely(nums: List[int]) -> bool:
    for i in range(len(nums)-1):
        num_diff = abs(nums[i] - nums[i+1])
        if nums[i] >= nums[i+1] or num_diff < 1 or num_diff > 3:
            return False

    return True

def is_decreasing_safely(nums: List[int]) -> bool:
    for i in range(len(nums)-1):
        num_diff = abs(nums[i] - nums[i+1])
        if nums[i] <= nums[i+1] or num_diff < 1 or num_diff > 3:
            return False

    return True





with open("day1/in.txt", "r") as f:
    lines = f.readlines()

result = 0
left_nums = []
right_nums = []

for line in lines:
    number_strings = line.split("   ")
    nums = [int(x) for x in number_strings]
    print(f"Number Pair: {nums}")
    left_nums.append(nums[0])
    right_nums.append(nums[1])

left_nums.sort()
right_nums.sort()

for i in range(len(left_nums)):
    print(f"Comparing {left_nums[i]} to {right_nums[i]}")
    result += abs(left_nums[i] - right_nums[i])

print(result)
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

for i in range(len(left_nums)):
    left_num = left_nums[i]
    matches = [r for r in right_nums if r == left_num]
    occurences = len(matches)
    print(f"Found {occurences} occurences of {left_num} in right nums")    
    result += left_num * occurences

print(result)
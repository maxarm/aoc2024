import regex
import os

print(os.getcwd())

with open("aoc2024/2023day1/inb.txt", "r") as f:
    lines = f.readlines()

pattern = r"(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)"
map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
       "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

result = 0
for line in lines:
    matches = regex.findall(pattern, line, overlapped=True)
    print(matches)
    line_result = map[matches[0]]*10 + map[matches[-1]]
    print(line_result)
    result += line_result
    
print(result)

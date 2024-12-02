# read lines from file
with open("2023day1/in.txt", "r") as f:
    lines = f.readlines()

result = 0

for line in lines:
    print(line)
    digits = [int(x) for x in line if x.isdigit()]
    lineResult = digits[0]*10 + digits[-1]
    print(lineResult)
    result += lineResult    

print(result)



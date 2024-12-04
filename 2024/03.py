import re

pat = r'mul\((\d+),(\d+)\)'
match = re.compile(pat)

with open('input/03.txt', 'r') as f:
    input = f.read().strip()

instructions = [(int(x[0]), int(x[1])) for x in re.findall(match, input)]

print(sum(x*y for x, y in instructions))

pat2 = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
match2 = re.compile(pat2)

instructions2 = re.findall(match2, input)

enabled = True
result = 0
for instruction in instructions2:
    if instruction == "don't()":
        enabled = False
    elif instruction == "do()":
        enabled = True
    if enabled:
        res = re.findall(match, instruction)
        if res:
            x, y = res[0]
            result += int(x) * int(y)

print(result)

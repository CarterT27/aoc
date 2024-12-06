from aoc_tools import *
import pyperclip

with open('input', 'r') as f:
    input = f.read()

lines = input.split('\n')

ans = ans_ = 0

disallowed = defaultdict(list)

for line in lines:
    if "|" in line:
        x, y = line.split('|')
        x, y = int(x), int(y)
        disallowed[y].append(x)
    elif ',' in line:
        update = [int(num) for num in line.split(',')]
        valid = True
        for i in range(len(update) - 1):
            d = disallowed[update[i]]
            remaining = set(update[i+1:])
            if any(n in remaining for n in d):
                valid = False
                break
        if valid:
            ans += update[len(update) // 2]

print(ans)
pyperclip.copy(ans)

def is_valid(update):
    valid = True
    for i in range(len(update) - 1):
        d = disallowed[update[i]]
        remaining = set(update[i+1:])
        if any(n in remaining for n in d):
            valid = False
            break
    return valid

for line in lines:
    if "|" in line:
        x, y = line.split('|')
        x, y = int(x), int(y)
        disallowed[y].append(x)
    elif ',' in line:
        update = [int(num) for num in line.split(',')]
        while not is_valid(update):
            for i in range(len(update) - 1):
                d = disallowed[update[i]]
                remaining = set(update[i+1:])
                for n in d:
                    if n in remaining:
                        j = update.index(n)
                        update[i], update[j] = update[j], update[i]
        ans += update[len(update) // 2]

print(ans)
pyperclip.copy(ans)

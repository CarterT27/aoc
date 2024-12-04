with open('input/02.txt', 'r') as f:
    input = f.readlines()
    input = [[int(x) for x in line.strip().split()] for line in input]

def is_safe(report):
    inc_or_dec = all(report[i] > report[i-1] for i in range(1, len(report))) or all(report[i] < report[i-1] for i in range(1, len(report)))
    if not inc_or_dec:
        return False
    return all(1 <= abs(report[i] - report[i-1]) <= 3 for i in range(1, len(report)))

print(sum(is_safe(report) for report in input))

def with_damper(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        skip = report[:i] + report[i+1:]
        if is_safe(skip):
            return True
    return False

print(sum(with_damper(report) for report in input))

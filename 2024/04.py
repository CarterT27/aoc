with open('input/04.txt', 'r') as f:
    input = f.read().split('\n')

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0),
        (1, 1)]

def bfs(row, col):
    xmas = 0
    for dr, dc in dirs:
        not_found = False
        for i, c in enumerate('XMAS'):
            new_row = row + i * dr
            new_col = col + i * dc
            if not (0 <= new_row < len(input) and 0 <= new_col < len(input)) or input[new_row][new_col] != c:
                not_found = True
                break
        if not not_found:
            xmas += 1
    return xmas

input = [row for row in input if row]
res = 0
for row in range(len(input)):
    for col in range(len(input[0])):
        if input[row][col] == 'X':
            res += bfs(row, col)

print(res)

diag = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

def bfs_2(row, col):
    xmas = 0
    for dr, dc in diag:
        not_found = False
        for i, c in enumerate('MAS'):
            new_row = row + dr - i * dr
            new_col = col + dc - i * dc
            if not (0 <= new_row < len(input) and 0 <= new_col < len(input)) or input[new_row][new_col] != c:
                not_found = True
                break
        if not not_found:
            xmas += 1
    return xmas > 1

res2 = 0
for row in range(len(input)):
    for col in range(len(input[0])):
        if input[row][col] == 'A':
            res2 += bfs_2(row, col)

print(res2)

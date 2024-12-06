from aoc_tools import *
import pyperclip

with open('input', 'r') as f:
    input = f.read()

input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

lines = [[c for c in line] for line in input.split('\n')]
visited = {}

ans = 0

di, dj = 0, 0
i_, j_ = 0, 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c in '^><v':
            if c == '^':
                di, dj = -1, 0
            elif c == '<':
                di, dj = 0, -1
            elif c == '>':
                di, dj = 0, 1
            elif c == 'v':
                di, dj = 1, 0
            print(c)
            print(di, dj)
            i_, j_ = i, j
i, j = i_, j_
lines[i][j] = 'X'
visited[(i, j)] = (di, dj)

n_rows, n_cols = len(lines), len(lines[0])
next_dir = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        }

num_can_place = 0
while 0 <= i+di < n_rows and 0 <= j+dj < n_cols:
    next_space = lines[i+di][j+dj]
    if next_space == '#':
        di, dj = next_dir[(di, dj)]
    diq, djq = next_dir[(di, dj)]
    if visited.get((i+diq, j+djq)) == (diq, djq):
        num_can_place += 1
    i, j = i+di, j+dj
    lines[i][j] = 'X'
    visited[(i, j)] = (di, dj)

lines = "\n".join("".join(line) for line in lines)
ans = lines.count('X')
ans = len(visited)
print(lines)
print(ans)
print(num_can_place)
pyperclip.copy(ans)

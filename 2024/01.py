import heapq
from collections import Counter

with open('input/01.txt', 'r') as f:
    input = f.readlines()

lst1 = []
lst2 = []

for line in input:
    n1, n2 = line.strip().split()
    lst1.append(int(n1))
    lst2.append(int(n2))

c2 = Counter(lst2)
lst1_copy = list(lst1)
heapq.heapify(lst1)
heapq.heapify(lst2)

total = 0
while lst1:
    total += abs(heapq.heappop(lst1) - heapq.heappop(lst2))

print(total)

similarity_score = 0

for num in lst1_copy:
    similarity_score += num * c2[num]

print(similarity_score)

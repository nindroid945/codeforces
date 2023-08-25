#https://codeforces.com/problemset/problem/263/A

matrix = []
steps = 0

for _ in range(5):
    n = input().split()
    matrix.append(n)

if "1" in matrix[0] or "1" in matrix[4]:
    steps += 2
if "1" in matrix[1] or "1" in matrix[3]:
    steps += 1

for i in range(5):
    if "1" in matrix[i]:
        pos = matrix[i].index("1")
        steps += abs(2 - pos)

print(steps)
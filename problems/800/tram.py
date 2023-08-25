#https://codeforces.com/problemset/problem/116/A

n = int(input())
max = 0
cur = 0

for i in range(n):
    exit, enter = map(int, input().split())
    cur = cur - exit + enter
    if cur > max:
        max = cur

print(max)
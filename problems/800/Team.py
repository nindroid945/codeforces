#https://codeforces.com/problemset/problem/231/A

n = int(input())

problems = 0
for _ in range(n):
    sol = input().split()
    if sol.count("1") >= 2:
        problems += 1

print(problems)
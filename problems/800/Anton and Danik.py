#https://codeforces.com/problemset/problem/734/A

n = int(input())
k = input()

a = 0
d = 0

for i in range(n):
    if k[i] == "A":
        a += 1
    elif k[i] == "D":
        d += 1

if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")
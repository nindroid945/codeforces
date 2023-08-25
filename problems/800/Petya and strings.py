#https://codeforces.com/problemset/problem/112/A

n = input().upper()
k = input().upper()

if n > k:
    print(1)
elif n < k:
    print(-1)
else:
    print(0)
#https://codeforces.com/problemset/problem/41/A

n = input()
k = input()

same = True
for i in range(len(n)):
    if n[-(i+1)] != k[i]:
        same = False
        break

if same:
    print("YES")
else:
    print("NO")
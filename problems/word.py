#https://codeforces.com/problemset/problem/59/A

n = input()

i = 0
upper = 0

for i in range(len(n)):
    if(n[i].isupper()):
        upper += 1

if upper > len(n) // 2:
    print(n.upper())
else:
    print(n.lower())

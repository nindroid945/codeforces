#https://codeforces.com/problemset/problem/546/A

banana = input().split(" ")

k, n, w = int(banana[0]), int(banana[1]), int(banana[2])

cost = 0
i = 0
for i in range(w):
    cost += (i+1)*k

if n > cost:
    print(0)
else:
    print(cost-n)
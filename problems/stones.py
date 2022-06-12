#https://codeforces.com/problemset/problem/266/A

n = int(input())
k = input()

count = 0
i = 0
for i in range(n-1):
    if(k[i+1] == k[i]):
        count += 1

print(count)


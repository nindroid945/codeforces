#https://codeforces.com/problemset/problem/791/A

n = input().split(" ")

limak = int(n[0])
bob = int(n[1])

count = 0
while bob >= limak:
    limak *= 3
    bob *= 2
    count += 1

print(count)

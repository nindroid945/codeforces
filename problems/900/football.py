#https://codeforces.com/problemset/problem/96/A

n = input()

consecutive = 0
dangerous = False
print(len(n))

for i in range(len(n)-1):
    print("i: " + str(i))
    if n[i] == n[i+1]:
        consecutive += 1
        #print("consecutive: " + str(consecutive))
        if consecutive >= 6:
            dangerous = True
    else:
        consecutive = 0

if dangerous:
    print("YES")
else:
    print("NO")
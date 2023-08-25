#https://codeforces.com/problemset/problem/160/A

n = int(input())
k = [int(x) for x in input().split()]

#print(k)
if n == 1:
    print(1)
elif n == 2:
    if k[0] == k[1]:
        print(2)
    else:
        print(1)
else:
    sum = 0
    for i in range(n):
        sum += k[i]
        
    count = 0
    val = 0
    while(val <= int(sum/2)):
        val += k.pop(k.index(max(k)))
        count += 1
    print(count)
    


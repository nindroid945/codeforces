#https://codeforces.com/problemset/problem/1632/A

testnum = int(input())

for _ in range(testnum):
    n = int(input())
    s = input()

    if len(s) == 1:
        print("YES")
    else:
        if list(s).count("0") >= 2 or list(s).count("1") >= 2:
            print("NO")
        else:
            print("YES")
    

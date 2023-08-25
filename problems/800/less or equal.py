#https://codeforces.com/problemset/problem/977/C

n, k = map(int, input().split())
lst = input().split()
seq = list(map(int, lst))
seq.sort()

seq2 = seq[0:k]

if seq[k] == seq[k+1]:
    print(-1)
else:
    print(seq[k-1])
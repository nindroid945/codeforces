#https://codeforces.com/problemset/problem/158/A

n, k = [int(x) for x in input().split()]
scores = input().split()

advancers = 0
if scores != []:
    target_score = int(scores[k-1])
    for score in scores:
        if int(score) >= target_score:
            if int(score) > 0:
                advancers += 1

print(advancers)

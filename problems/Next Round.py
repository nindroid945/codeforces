n, k = [int(x) for x in input().split()]
scores = input().split()

advancers = 0
for score in scores:
    if score >= scores[k]:
        if score > 0:
            advancers += 1

print(advancers)

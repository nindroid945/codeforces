#https://codeforces.com/problemset/problem/1411/B

n = int(input())

for _ in range(n):
    num = int(input())
    digits = [int(x) for x in str(num)]
    while 0 in digits:
        digits.remove(0)

    not_fair = True

    for dig in digits:
        if num % dig == 0:
            not_fair = False
    
    while not_fair:
        num += 1
        for dig in digits:
            if num % dig != 0:
                not_fair = False
    
    if not_fair == False:
        print(num)


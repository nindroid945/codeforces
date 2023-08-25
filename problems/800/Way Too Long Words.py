#https://codeforces.com/problemset/problem/71/A

n = int(input())

for _ in range(n):
    word = input()
    if len(word) > 10:
        inside_letters = word[1:len(word)-1]
        print(word[0] + str(len(inside_letters)) + word[-1])
    else:
        print(word)

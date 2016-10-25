import math

N = input()
s = input().split()
s = map(int, s)
total = sum(s)
if total < 10 ** 9:
    if total <
        answer = 1
else:
    answer = math.ceil(sum(s) / 10 ** 9)
print(answer)

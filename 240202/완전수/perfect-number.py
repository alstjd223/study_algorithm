s, e = map(int, input().split())
b = 0
for i in range(s, e+1):
    a = []
    for j in range(1, i):
        if i % j == 0:
            a.append(j)
    if sum(a) == i:
        b += 1
print(b)
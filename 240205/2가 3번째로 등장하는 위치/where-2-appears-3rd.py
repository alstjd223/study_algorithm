n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if cnt == 3:
        print(i+1)
        break
    if a[i] == 2:
        cnt += 1
        if cnt == 3:
            print(i+1)
            break
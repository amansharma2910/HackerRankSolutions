n = int(input())
if 0 < n <= 1000:
    sum = 0
    flag = 1
    ar = list(map(int, input().split()))
    for i in ar:
        if 0 < i <= 1000:
            sum += i
        else:
            flag = 0
            break
    if flag == 1:
        print(sum)
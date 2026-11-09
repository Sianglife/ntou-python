n, k = map(int, input().split())
l = list(map(int, input().split()))

start = 0
end = n - 1
leng = end - start + 1
founded = False

while founded == False:
    sum = 0
    for i in range(start, end + 1):
        sum += l[i]
    # print(f"leng: {leng}, start: {start}. end: {end}, sum: {sum}")
    if sum > k:
        # Move window
        if end != (n - 1):
            start += 1
            end += 1
        else:
            leng -= 1
            start = 0
            end = leng - 1
    else:
        founded = True

print(leng)

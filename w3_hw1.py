n = int(input())

for _ in range(n):
    s = input()
    count = {}

    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    ans = max(count, key=count.get)
    print(ans)
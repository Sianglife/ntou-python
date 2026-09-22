n = int(input())

for _ in range(n):
    s = input()
    max_val = 0
    feq = {}
    for char in s:
        if char in feq:
            feq[char] += 1
        else:
            feq[char] = 1
        if max_val < feq[char]:
            max_str = char
            max_val = feq[char]

    print(max_str)
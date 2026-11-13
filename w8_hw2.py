full_str = input()
small_str = input()

LPS = [0]

prevLPS, i = 0, 1

# gen LPS
while i < len(small_str):
    if small_str[i] == small_str[prevLPS]:
        LPS.append(prevLPS + 1)
        prevLPS += 1
        i += 1
    elif prevLPS == 0:
        LPS.append(0)
        i += 1
    else:
        prevLPS = LPS[prevLPS - 1]

# print(LPS)


i ,j = 0, 0
while i < len(full_str):
    if full_str[i] == small_str[j]:
        i, j = i+1, j+1
    elif j == 0:
        i += 1
    else: 
        j = LPS[j - 1]
    if j == len(small_str):
        print(i - len(small_str), end=" ")
        j =  LPS[j - 1]
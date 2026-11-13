move = [
    [0, -1], # 左
    [0, 1], # 右
    [-1, 0], # 上
    [1, 0] # 下
]

h, w = map(int, input().split())
maze = []
mark =[[False for _ in range(w)] for __ in range(h)]
# print(mark)
vert, hori = 0, 0

for i in range(h):
    row = [char for char in input()]
    # print("row", row)
    for j in range(w):
        # print("j", j)
        if row[j] == "S":
            hori = j
            vert = i
    maze.append(row)

founded = False
mark[vert][hori] = True
dir = -1

route = []



while not founded:
    while dir < 3:
        dir += 1
        # print("r:", route, 'd:', dir)
        next_vert = vert + move[dir][0]
        next_hori = hori + move[dir][1]

        # out of range detect
        if next_vert < 0 or next_vert >= h or next_hori < 0 or next_hori >= w:
            # print('pass', next_vert, next_hori)
            continue

        if maze[next_vert][next_hori] == "T":
            route.append([next_vert, next_hori])
            founded = True
            # print('found', next_vert, next_hori)
            break

        if mark[next_vert][next_hori] == True or maze[next_vert][next_hori] == '#':
            # print('pass2', next_vert, next_hori, mark[next_vert][next_hori])
            continue

        # print('next', next_vert, next_hori)
        # print('cur', vert, hori)
        mark[vert][hori] = True
        # print('set', vert, hori)
        route.append([vert, hori, dir])
        # print('mark', mark)
        vert = next_vert
        hori = next_hori
        dir = 0



    if not founded:
        print(-1)
        break
if founded:
    print(len(route))




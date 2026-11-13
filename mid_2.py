n, q = map(int, input().split())
mult = list(map(int, input().split()))
next_avail = [0 for _ in range(n)]

for i in range(q):
    arrival_time, basic_wash_time, max_wait = map(int, input().split())
    min_finish = 99999
    # print('next_avail:', next_avail)
    for it, nex in enumerate(next_avail):
        if nex - arrival_time > max_wait:
            continue
        # print('mult:', mult[it], 'id:', it)
        start_time = max(arrival_time, nex)
        new_finish_time = start_time + basic_wash_time * mult[it]
        # print('new finish:', new_finish_time)
        if min_finish > new_finish_time:
            min_id = it
            min_start = start_time
            min_finish = new_finish_time
    if min_finish == 99999:
        print("REJECTED")
    else:
        # print('id+1:', min_id+1, 'start:', min_start, 'finish:', min_finish)
        print(min_id + 1, min_start, min_finish)
        next_avail[min_id] = min_finish

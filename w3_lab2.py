n = int(input())
# Each Test Case
while True:
    target = list(map(int, input().split()))
    if int(target[0]) == 0:
        break
    
    targetidx = 0

    a = list(range(n, 0, -1))
    stack = []
    results = []

    while len(a) > 0:
        stack.append(a.pop())

        while len(stack) > 0 and targetidx < n and stack[-1] == target[targetidx]:
            results.append(stack.pop())
            # print(f"pop {results[-1]} and results is {results} and targetidx is {targetidx} and target is {target}")
            targetidx += 1

    
    if targetidx == n:
        print("YES")
    else:
        print("NO")
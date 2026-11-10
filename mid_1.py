ori_str = input()
stack = []
cur_pattern = []
times_str = ""
for char in ori_str:
    if char != ']':
        stack.append(char)
        # print('push', stack[-1])
    else:
        while stack[-1] != '[':
            cur_pattern.append(stack[-1])
            # print('pop', stack[-1])
            stack.pop()
        
        # print('pop', stack[-1])
        stack.pop()
        while stack and stack[-1].isdigit():
            times_str += stack[-1]
            # print('pop', stack[-1])
            stack.pop()
        # print(times_str[::-1])
        times = int(times_str[::-1])
        times_str = ""
        stack.append(times * "".join(cur_pattern[::-1]))
        # print('push', stack[-1]) 
        cur_pattern = []
print("".join(stack))
print(len("".join(stack)))
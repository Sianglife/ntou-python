n, m = list(map(int, input().split()))
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

mutual = a.intersection(b)
print(len(mutual))
print("".join(map(lambda x: str(x) + " ", sorted(mutual))))
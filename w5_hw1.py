from functools import wraps

def cache_decorator(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(f"now: {args[0]}")
        if args[0] in cache:
            print(f"Cache hit for fibonacci({args[0]})")
            return cache[args[0]]
        else:
            cache[args[0]] = func(args[0])
            print(f"Computed fibonacci({args[0]}) = {cache[args[0]]}")
            
        return cache[args[0]]

    return wrapper

@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    # print(f"next: {n - 1}, {n - 2}, n: {n}")
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input().strip())
print(f"Final Result: {fibonacci(n)}")
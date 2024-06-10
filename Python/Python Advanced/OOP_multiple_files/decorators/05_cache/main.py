def cache(func_ref):
    def wrapper(num):
        cache_key = num
        if cache_key not in wrapper.log:
            wrapper.log[cache_key] = func_ref(num)

        return wrapper.log[cache_key]
    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)

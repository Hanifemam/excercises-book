def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))


def fib_iterative(n):
    n_min_two = 0
    n_min_one = 1
    i = 2
    while i <= n:
        new_val = n_min_two + n_min_one
        n_min_two = n_min_one
        n_min_one = new_val
        i += 1
    return new_val


print(fib_iterative(8))

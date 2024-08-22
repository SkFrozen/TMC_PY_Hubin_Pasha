def fib(n):
    fib_1 = 1
    fib_2 = 1
    counter = 0

    while counter < n:
        counter += 1
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        yield fib_2


for el in fib(10):
    print(el)

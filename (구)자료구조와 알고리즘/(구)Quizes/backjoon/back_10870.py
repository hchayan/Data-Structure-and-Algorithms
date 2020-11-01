


def fibonacci(num):
    f1, f2 = 0, 1
    for i in range(num):
        f1, f2 = f2, f1+f2
    return f1

print(fibonacci(int(input())))
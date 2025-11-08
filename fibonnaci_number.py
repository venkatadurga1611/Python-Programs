def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

n = int(input("Enter Position : "))
r = fibonacci(n)
print(f"The {n}th position of a number is {r}")

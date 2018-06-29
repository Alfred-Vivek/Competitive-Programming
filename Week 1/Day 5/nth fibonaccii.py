def fib(n):
    a = 0
    b = 1
    if n < 0:
        raise ValueError("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(0,n-1):
            c = a + b
            a = b
            b = c
        return b
 
# Test Cases

actual = fib(0)
expected = 0
print(actual == expected)

actual = fib(1)
expected = 1
print(actual == expected)

actual = fib(2)
expected = 1
print(actual == expected)

actual = fib(3)
expected = 2
print(actual == expected)

actual = fib(5)
expected = 5
print(actual == expected)

actual = fib(10)
expected = 55
print(actual == expected)
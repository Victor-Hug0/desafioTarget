def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

number = 4
sequence = fibonacci(20)

if number in sequence:
    print(f"{number} pertence a sequência de Fibonacci!")
else:
    print(f"{number} não pertence a sequência de Fibonacci!")
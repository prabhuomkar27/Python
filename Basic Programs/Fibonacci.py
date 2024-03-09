def fibonacci(n):
    fib_sequence=[0,1]

    while len(fib_sequence)<n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

user_input = int(input("Enter the number of Fibonacci elements you want : "))

if user_input<=0:
    print("Please enter a positive integer")
else:
    fibonacci_sequence = fibonacci(user_input)
    print("Fibonacci sequence:", fibonacci_sequence)


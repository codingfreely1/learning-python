fibonacci_arr = [1, 1]


def fibonacci(n):
    if n == 0:
        return fibonacci_arr[0]
    if n == 1:
        return fibonacci_arr[1]

    if n < len(fibonacci_arr):
        return fibonacci_arr[n]
    else:
        fibonacci_arr.insert(n, fibonacci(n-1) + fibonacci(n-2))
        return fibonacci_arr[n]


def main():
    n = raw_input('How many numbers in the sequence to generate? ')
    if int(n) >= 0:
        for i in range(0, int(n)):
            print(fibonacci(i))
    else:
        print 'invalid input'


main()
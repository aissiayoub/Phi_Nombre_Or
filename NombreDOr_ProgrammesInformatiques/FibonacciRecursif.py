import sys


def fibonacci(n):

    print(n)
            
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def main():
    print(fibonacci(20))

main()


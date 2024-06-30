
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f1 = 0
        f2 = 1
        for i in range(n-2):
            temp = f2
            f2 = (f1 + f2)
            f1 = temp
        return f1 + f2

if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )

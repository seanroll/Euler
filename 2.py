if __name__ == "__main__":
    s = 2
    a = 3
    fib = [1,2]
    while a <= 4000000:
        fib.append(a)
        if a % 2 == 0:
            s += a
        a = fib[-1] + fib[-2]
    print(s)
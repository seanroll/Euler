
def next_collatz(n):
    if n != 1:
        if n % 2 == 0:
            return n / 2
        return 3 * n + 1


if __name__ == '__main__':
    depths = {1 : 0}
    for i in range(2,1000000):
        a = i
        d = 0
        while a not in depths.keys():
            a = next_collatz(a)
            d+=1
        d+=depths[a]
        depths[i] = d

    max_key = 1
    for key in depths.keys():
        if depths[key] > depths[max_key]:
            max_key = key
    print(max_key)

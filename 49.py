from tools import prime


def list_mod_k(arr, k):
    return [e % k for e in arr]


def digit_repr(n):
    return [str(n).count(str(i)) for i in range(10)]


if __name__ == "__main__":
    primes_under_10000 = prime.sieve(10000)
    for i in prime.sieve(1000):
        primes_under_10000.remove(i)

    for d in range(6, 4455, 6):
        l = list_mod_k(primes_under_10000, d)
        for n in l:
            if l.count(n) == 3:
                if digit_repr(n) == digit_repr(n + d) == digit_repr(n + 2 * d):
                    print(n, n + d, n + 2 * d)

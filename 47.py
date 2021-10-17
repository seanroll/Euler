from tools import prime

def find_num_distinct_factors(n):
    f = 0
    for p in prime.sieve(n):
        if not n % p:
            f+=1
    return f

if __name__ == "__main__":
    chain = 0
    n = 133330
    while chain < 4 and n < 150000:
        if find_num_distinct_factors(n) == 4:
            chain+=1
            print(n)
        else:
            chain = 0
        n+=1
    print(n-4)
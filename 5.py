from tools import prime
from math import *

if __name__ == "__main__":
    product = 1
    for prime in prime.sieve(20):
        product *= pow(prime,floor(log(20,prime)))
    print(product)
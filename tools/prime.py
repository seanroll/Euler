from math import *
def sieve(n):

    a = [True for i in range(n+1)]
    for i in range(2, ceil(sqrt(n))):
        if a[i]:
            for j in range(i*i,n+1,i):
                a[j] = False
    a[0] = False
    a[1] = False

    b=[]
    for k in range(len(a)):
        if a[k]:
            b.append(k)
    return b

def is_prime(n):
    return (n in sieve(n+1))

if __name__ == "__main__":
    print(sieve(10))
    print(is_prime(1901245))
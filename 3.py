from tools import prime

if __name__ == "__main__":
    a = 2007
    i = 2
    while a % i and i*i < a:
        i+=1
        if not a % i:
            a /= i
            i = 2
    print(a)
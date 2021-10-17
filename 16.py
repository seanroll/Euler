if __name__ == "__main__":
    x = 2**1000
    s = 0
    while x:
        s+=x % 10
        x//=10
    print(s)
import math

def find_x_given_minimal_soln(D):
    if not math.sqrt(D) % 1:
        return 0
    x = math.ceil(math.sqrt(D))
    while math.sqrt((-1 + x*x)/D) % 1:
        x+=1
    return x

if __name__ == "__main__":
    s = []
    for D in range(1001):
        print(D)
        s.append(find_x_given_minimal_soln(D))
    print(s.index(max(s)))
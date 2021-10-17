import math

def sum_of_digits_factorial(n):
    s = 0
    for c in str(n):
        s += math.factorial(int(c))
    return s

if __name__ == "__main__":
    nums = []
    for i in range(10,10000000):
        if i == sum_of_digits_factorial(i):
            nums.append(i)
    print(nums)
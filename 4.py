if __name__ == "__main__":
    largest_palindrome = 0
    for i in range(1,1000):
        for j in range(1,1000):
            if str(i*j) == str(i*j)[::-1]:
                if i*j > largest_palindrome:
                    largest_palindrome = i*j
    print(largest_palindrome)
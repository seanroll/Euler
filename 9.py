if __name__ == "__main__":
    # m(m+n) = 500
    for m in range(1, 501):
        if not 500 / m % 1:
            n = 500 / m - m
            if 0 < n < m:
                print((m ** 2 - n ** 2)*( 2 * m * n)*(m ** 2 + n ** 2))

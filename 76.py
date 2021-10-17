
def num_of_partitions(n):
    # dp[i][j] represents the number of sums equal to i+1 with highest term j+1
    dp = []
    for i in range(n):
        dp.append([0] * n)

    for i in range(n):
        for j in range(n):
            if j == 0 or i == j:
                dp[i][j] = 1
            elif j > i:
                dp[i][j] = 0
            else:
                dp[i][j] = sum(dp[i - j - 1][:j + 1])
    return sum(dp[-1])


if __name__ == "__main__":
    num_of_partitions(100) - 1
if __name__ == "__main__":
    p = [[0]*21]*21
    for i in range(21):
        for j in range(21):
            if i==0 or j==0:
                p[i][j] = 1
            else:
                p[i][j] = p[i-1][j] + p[i][j-1]
    print(p[20][20])
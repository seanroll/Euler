if __name__ == "__main__":
    # converts the txt file into a 2d array of numbers
    f = open("18.txt")
    tri = []
    sums = []
    for line in f:
       tri.append([])
       sums.append([])
       for num in line[:-1].split(" "):
            tri[-1].append(int(num))
            sums[-1].append(0)
    tri[-1][-1] = 23

    sums[0][0] = tri[0][0]
    sums[1][0] =  tri[0][0] + tri[1][0]
    sums[1][1] =  tri[0][0] + tri[1][1]

    for i in range(2, len(tri)):
       for j in range(i+1):
               if j==0:
                   sums[i][j] = sums[i-1][j] + tri[i][j]
               elif j== i:
                   sums[i][j] = sums[i - 1][j-1] + tri[i][j]
               else:
                   sums[i][j] = tri[i][j] + max(sums[i-1][j-1], sums[i-1][j])

print(max(sums[-1]))

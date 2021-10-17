if __name__ == "__main__":
    solns = [0]*501
    for p in range(501):
        m = 1
        while m < p:
            if not p % m:
                if m > p/m - m and p/m - m > 0:
                    solns[p] +=1
                    print(2*p, m, p/m - m)
            m+=1
    print(max(solns))

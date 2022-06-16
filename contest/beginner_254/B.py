def main():
    n = int(input())
    a = [[1] for i in range(n)]

    for i in range(1, n):
        for j in range(1, i+1):
            if i == j:
                a[i].append(1)
            else:
                a[i].append(a[i-1][j-1] + a[i-1][j])

    for ai in a:
        s = ''
        for aij in ai:
            s += str(aij) + ' '
        print(s)


if __name__ == '__main__':
    main()

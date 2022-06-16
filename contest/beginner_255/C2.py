def main():
    x, a, d, n = map(int, input().split())

    if d < 0:
        x = -x
        a = -a
        d = -d

    le = 0
    ri = n-1
    while ri - le > 1:
        m = (le + ri) // 2
        s = a + d*m
        if x < s:
            ri = m
        else:
            le = m

    print(min(abs(x-a-d*le), abs(x-a-d*ri)))


if __name__ == '__main__':
    main()

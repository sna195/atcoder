def main():
    n = int(input())
    t = x = y = 0
    flg = True
    for i in range(n):
        tg, xg, yg = map(int, input().split())
        d = abs(x-xg) + abs(y-yg)
        td = tg - t
        if td < d or abs(td-d) % 2 != 0:
            flg = False
            break
        x = xg
        y = yg
        t = tg

    if flg:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()

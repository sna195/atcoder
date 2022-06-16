def main():
    n, y = map(int, input().split())
    a = 10000
    b = 5000
    c = 1000
    cnt_a = 0
    cnt_b = 0
    cnt_c = y / c
    cnt_all = 0

    cnt_all += cnt_c
    sub_max = cnt_all - n
    sub_min = c
    if sub_max < 0:
        print('-1 -1 -1')
    if sub_min > 0


if __name__ == '__main__':
    main()

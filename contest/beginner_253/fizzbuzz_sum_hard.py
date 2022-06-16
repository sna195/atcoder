def main():
    n, a, b = map(int, input().split())

    cnt = n * (n + 1)
    cnt = int(cnt / 2)

    n_a = n // a
    cnt_a = n_a * (a * n_a + a)
    cnt_a = int(cnt_a / 2)

    n_b = n // b
    cnt_b = n_b * (b * n_b + b)
    cnt_b = int(cnt_b / 2)

    c = a * b
    n_c = n // c
    cnt_c = n_c * (c * n_c + c)
    cnt_c = int(cnt_c / 2)

    print(cnt - cnt_a - cnt_b + cnt_c)


if __name__ == '__main__':
    main()

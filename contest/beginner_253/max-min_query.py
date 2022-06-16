def que_1(s, x, cnt):
    cnt[x] += 1
    s.append(x)
    return s, cnt


def que_2(s, x, c, cnt):
    [s.remove(x) for i in range(min(c, cnt[x]))]
    return s


def que_3(s):
    if len(s) == 0:
        print(-1)
    else:
        print(max(s) - min(s))


def main(q, que):
    s = []
    cnt = [0] * (10**9 + 1)

    for i in range(q):
        new_query = que[i]

        if new_query[0] == 1:
            s, cnt = que_1(s, int(new_query[1]), cnt)
        elif new_query[0] == 2:
            s = que_2(s, int(new_query[1]), int(new_query[2]), cnt)
        else:
            que_3(s)


if __name__ == '__main__':
    Q = int(input())
    QUE = [list(map(int, input().split())) for i in range(Q)]
    main(Q, QUE)

def main():
    q = int(input())
    que = [input() for i in range(q)]
    s = []
    cnt = [0] * (10**9 + 1)

    for i in range(q):
        new_query = que[i]

        if new_query[0] == '1':
            x = int(new_query[2])
            cnt[x] += 1
            s.append(x)

        elif new_query[0] == '2':
            x = int(new_query[2])
            c = int(new_query[4])
            for j in range(min(c, x)):
                s.remove(x)
        else:
            if len(s) == 0:
                print(-1)
            else:
                print(max(s) - min(s))


if __name__ == '__main__':
    main()

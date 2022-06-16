def main():
    N = int(input())
    S = [input() for i in range(N)]

    cnt = [[-1] for i in range(10)]
    score = 0

    for i in range(N):
        for j in range(10):
            s = int(S[i][j])
            score += j
            h = 0
            for k in range(1, len(cnt[s])):
                if j + 10*h == cnt[s][k]:
                    score += 10
                    h += 1
            cnt[s].append(score)
            score = 0

    ans = []
    for i in range(len(cnt)):
        ans.append(max(cnt[i]))
    ans.sort(reverse=True)
    print(ans.pop())


if __name__ == '__main__':
    main()
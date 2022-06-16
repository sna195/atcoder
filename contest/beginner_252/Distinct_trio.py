def dpm():
    N = int(input())
    freq = [0] * (2 * 10**5 + 10)
    for a in map(int, input().split()):
        freq[a] += 1
    dp = [1, 0, 0, 0, 0]
    for f in freq:
        nx = [0] * 5
        for i in range(4):
            nx[i + 1] += dp[i] * f
            nx[i] += dp[i]
        dp = nx
    print(dp[3])


def main(n, a):
    num_ai = []

    while a:
        b = a[0]
        count = 1
        for i in range(1, len(a)):
            if b == a[i]:
                count += 1
            else:
                continue
        [a.remove(b) for j in range(count)]
        num_ai.append([b, count])

    num_ai = sorted(num_ai, key=lambda x: x[0])
    la = len(num_ai)

    com = [[num_ai[0][1], 0]]
    num_con = 0
    for i in range(1, la):
        num_con += num_ai[i-1][1]
        com.append([num_ai[i][1], num_con])

    ans = 0
    com.reverse()
    lc = len(com)
    for i in range(lc-2):
        for j in range(i+1, lc-1):
            ans += com[i][0] * com[j][0] * com[j][1]

    print(ans)


if __name__ == '__main__':
#    N = int(input())
#    A = list(map(int, input().split()))
#    main(N, A)
    dpm()

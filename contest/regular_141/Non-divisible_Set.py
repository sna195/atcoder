def main(n, m, a):
    s = 2*m

    for ai in a:
        ans = 'No'
        cnt = 0
        flg = True
        nu = []

        if ai < m:
            for j in range(m):
                if (s-j) % ai != 0:
                    cnt += 1
                    nu.append(s-j)
                else:
                    continue
                if cnt >= m:
                    ans = 'Yes'
                    flg = False
                    break

            if flg:
                for j in range(m):
                    if (m-j) % ai != 0:
                        lu = len(nu)
                        for u in nu:
                            if u % (m-j) == 0:
                                lu -= 1
                            if lu == 0:
                                nu.append(m-j)
                                cnt += 1

                    if cnt >= m:
                        ans = 'Yes'
                        break

        elif ai >= m:
            cnt = s-ai
            [nu.append(s-i-1) for i in range(s-ai)]
            if s % ai != 0:
                cnt += 1
                nu.append(s)

            if flg:
                for j in range(ai-1):
                    if (ai-j-1) % ai != 0:
                        lu = len(nu)
                        for u in nu:
                            if u % (ai-j-1) != 0:
                                lu -= 1
                            if lu == 0:
                                nu.append(ai-j-1)
                                cnt += 1

                    if cnt >= m:
                        ans = 'Yes'
                        break

        print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    main(N, M, A)

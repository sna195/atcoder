def main():
    n = int(input())

    ans = 0
    for i in range(1, n+1):
        q = i**2
        ans += 1
        if q/n < n:
            for j in range(1, i):
                if q % j == 0 and q / j <= n:
                    ans += 2

    print(ans)


if __name__ == '__main__':
    main()

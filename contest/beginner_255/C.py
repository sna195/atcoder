def main():
    x, a, d, n = map(int, input().split())
    s = a
    ans = abs(x-a)
    for i in range(1, n):
        s += d
        if abs(x-s) <= abs(d):
            ans = min(abs(x-s), abs(x-s-d))
            break
    if s == a + d*(n-1):
        ans = abs(x-s)

    print(ans)



if __name__ == '__main__':
    main()

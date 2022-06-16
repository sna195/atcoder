def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    like = max(a)
    flag = False

    for i in range(k):
        if a[b[i] - 1] == like:
            flag = True


    print(ans)


if __name__ == '__main__':
    main()

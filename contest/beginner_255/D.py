def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(q):
        x = int(input())
        s = 0
        for aj in a:
            s += abs(aj - x)
        print(s)


if __name__ == '__main__':
    main()

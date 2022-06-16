def main():
    n = int(input())
    d = [int(input()) for i in range(n)]

    d = set(d)
    print(len(d))


if __name__ == '__main__':
    main()

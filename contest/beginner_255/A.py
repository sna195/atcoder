def main():
    r, c = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(r)]
    print(a[r-1][c-1])

if __name__ == '__main__':
    main()

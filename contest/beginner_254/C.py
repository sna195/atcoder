def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    flag = 1
    while flag:
        flag = 0
        for i in range(n-k):
            if a[i] > a[i+k]:
                flag = 1
                t = a[i]
                a[i] = a[i+k]
                a[i+k] = t

    ans = 'Yes'
    for i in range(n-1):
        if a[i] > a[i+1]:
            ans = 'No'
            break

    print(ans)

if __name__ == '__main__':
    main()

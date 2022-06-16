def f(s):
    s_first = s.pop(0)
    s.append(s_first)

    return s

def main():
    N, K = map(int, input().split())
    S = input()

    T = S
    char_count = [T.p]

    print(ans)


if __name__ == '__main__':
    main()
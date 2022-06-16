def judge_original(A, a):
    for j in range(1, len(A)):
        if A[j][0] == a:
            return False
        else:
            continue
    return True


def main():
    N = int(input())

    A = [list(input().split()) for j in range(N)]
    A = dict(zip([j + 1 for j in range(N)], A))

    A = sorted(A.items(), key=lambda x:int(x[1][1]))

    while len(A) > 0:
        a = A.pop()
        if judge_original(A, a[1][0]):
            print(a[0])
            break
        else:
            continue

if __name__ == '__main__':
    main()

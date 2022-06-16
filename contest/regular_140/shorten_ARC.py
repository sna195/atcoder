def search_ARC(s):
    cnt_replace = []
    for i in range(len(s) - 2):
        if s[i+2] == 'A':
            i += 1
        elif s[i:i+3] == 'ARC':
            j = 1
            while i-j >= 0 and i+j+2 < len(s) and s[i-j] == 'A' and s[i+j+2] == 'C':
                j += 1
            cnt_replace.append(j)
            i += j + 1
        else:
            continue

    cnt_replace.sort()
    return cnt_replace


def main():
    N = int(input())
    S = input()

    rep = search_ARC(S)
#    ans = 0
#
#    cnt_len = len(rep)
#    if rep:
#        while cnt_len > 0:
#            cnt = rep.pop()
#            cnt_len = cnt_len - cnt + 1
#            ans += 2 * (cnt - 1)
#            rep.append(1)
#
#        ans += 2 * cnt_len
#        if cnt_len < 0:
#            ans += 1
#    else:
#        ans = 0

    print(min(2*len(rep), sum(rep)))


if __name__ == '__main__':
    main()

h, w = map(int, input().split())
s = [input() for i in range(h)]

start_h = []
start_w = []
cnt = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            start_h.append(i)
            start_w.append(j)
            if cnt > 1:
                break
            else:
                cnt += 1

ans = abs(start_h[0] - start_h[1]) + abs(start_w[0] - start_w[1])

print(ans)


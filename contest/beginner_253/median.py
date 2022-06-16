a, b, c = map(int, input().split())

ans = 'No'
if a <= b <= c or c <= b <= a:
    ans = 'Yes'

print(ans)

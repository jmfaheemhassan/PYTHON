t = int(input())
for _ in range(t):
    s = input().strip()
    idx0 = s.index('0')
    s = s[:idx0] + s[idx0+1:]
    idx1 = s.index('1')
    s = s[:idx1] + s[idx1+1:]
    print(s)
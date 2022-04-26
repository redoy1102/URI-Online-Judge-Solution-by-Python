def bro(M, N):
    sum = 0
    if M < N:
        for x in range(M, N + 1):
            sum += x
            print(x, end=' ')
        print('Sum=%d' % sum)

    else:
        for x in range(N, M + 1):
            sum += x
            print(x, end=' ')
        print('Sum=%d' % sum)

while True:
    M, N = [int(x) for x in input().split()]
    if M > 0 and N > 0:
        bro(M, N)
    else:
        break

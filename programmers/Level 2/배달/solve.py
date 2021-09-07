def solution(N, road, K):
    a = [[999999 for i in range(N)] for i in range (N)]
    for x,y,time in road:
        if a[x-1][y-1] > time:
            a[x-1][y-1] = time
            a[y-1][x-1] = time

    for i in range (N):
        a[i][i] = 0

    for k in range (N):
        for x in range (N):
            for y in range (N):
                if a[x][y] > a[x][k] + a[k][y]:
                    a[x][y] = a[x][k] + a[k][y]
                    a[y][x] = a[x][k] + a[k][y]

    cnt = 0
    for i in a[0]:
        if i <= K:
            cnt += 1
    return cnt
    
    



N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 3

print(solution(N, road, K))

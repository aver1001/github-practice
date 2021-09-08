from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solution(board):
    answer = 0

    N = len(board)
    start, end = (0, 0), (N - 1, N - 1)
    costs = [[float('inf')] * N for _ in range(N)]

    deq = deque()
    deq.append((0, 0, 0, 1))
    deq.append((0, 0, 0, 3))
    costs[0][0] = 0
    ## 오른쪽이 먼져냐 아래가 먼져냐의따라 예제가 달라짐.
    ## 그래서 두개다 해서 최솟값 내보내면 될 것 같음 
    while deq:
        
        x, y, cost, dir = deq.popleft()
        for i in costs: print(i)
        print()
        for k in range(4):
            tmp_cost = cost
            ##방향
            nx = x + dx[k]
            ny = y + dy[k]
            ## 방향의 따른 cost 정해줌
            if dir != k : tmp_cost += 1
            ## 범위안에 있으면
            if 0 <= nx < N and 0 <= ny < N:
                ## 길이 막혀있지 않고, 가격이 더 쌀경우
                if board[nx][ny] == 0 and tmp_cost <= costs[nx][ny]:
                    ##코스트의 가격을 업데이트 해주고
                    costs[nx][ny] = tmp_cost
                    ## 큐에 넣어줌
                    deq.append((nx, ny, tmp_cost, k))

    answer = costs[end[0]][end[1]]

    return answer

    
solution([
[0, 0, 0, 0, 0], 
[0, 1, 1, 1, 0], 
[0, 0, 1, 0, 0], 
[1, 0, 0, 0, 1], 
[0, 1, 1, 0, 0]
])

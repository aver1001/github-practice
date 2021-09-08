def solution(board):
    a = len(board)
    b = len(board[0])
    if a == 1 and b == 1:
        if board[0][0] == 1:
            return 1
        else:
            return 0
    answer = 0
    for i in range(1,a):
        for j in range(1,b):
            for k in board: print(k)
            print()
            if board[i][j] != 0:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
                if board[i][j] > answer:
                    answer = board[i][j]
    return answer
        
solution([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

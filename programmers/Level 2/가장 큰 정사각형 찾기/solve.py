def check (x,y,n,board):
    for i in range (n):
        for j in range (n):
            if board[x+i][y+j] != 1:
                return False
    return True

def solution(board):
    a = len(board)
    b = len(board[0])
    n = min(a,b)
    while(True):
        print(n)
        for i in range (a-n+1):
            for j in range (b-n+1):
                if check(i,j,n,board):
                    return n*n
        n -= 1
        
## 효율성 탈락

def solution(n, results):

    table = [[0 for _ in range (n)]for _ in range (n)]
    for a,b in results:
        table[a-1][b-1] = 1
        table[b-1][a-1] = -1
    for i in table : print(i)
    print()
        
        
    for k in range (n):
        for i in range (n):
            for j in range (n):
                if table[i][j] == 0:
                    if table[i][k] == 1 and table[k][j] == 1:
                        table[i][j] = 1
                        table[j][i] = -1
                    elif table[i][k] == -1 and table[k][j] == -1:
                        table[i][j] = -1
                        table[j][i] = 1
                        
    cnt = 0
    for i in table:
        if i.count(0) == 1:
            cnt += 1

    return cnt

        


solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])

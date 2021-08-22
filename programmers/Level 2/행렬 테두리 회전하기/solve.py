def solution(rows, columns, queries):
    ## 행렬 생성
    matrix = []
    cnt = 1
    for i in range(rows):
        temp = []
        for j in range(colums):
            temp.append(cnt)
            cnt +=1
        matrix.append(temp)
    add = [[0,1],[1,0],[0,-1],[-1,0]]
    answer = []
    for i in queries:
        ## 꼭짓점 분리
        vertex = [[i[0]-1,i[1]-1],[i[0]-1,i[3]-1],[i[2]-1,i[3]-1],[i[2]-1,i[1]-1]]
        x,y = vertex[0]
        temp = matrix[x][y]
        queue = []
        cnt = 0
        for i in add:
            while(True):
                queue.append(matrix[x][y])
                x += i[0]
                y += i[1]
                if [x,y] in vertex:
                    break
        answer.append(min(queue))
        queue.insert(0,queue.pop())
        x,y = vertex[0]
        for i in add:
            while(True):
                matrix[x][y] = queue.pop(0)
                x += i[0]
                y += i[1]
                if [x,y] in vertex:
                    break
                            
    return answer



rows = 6
colums = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

a = solution(rows,colums,queries)    



def solution(n, computers):
    check = [0 for _ in range (n)]
    queue = []
    network = 0

    ##computers 배열을 돌며
    for i in range(n):

        ## 한번도 간 적이 없는 컴퓨터이면 네트워크 +1 해준다
        if check[i] == 0:
            network += 1

            #그 컴퓨터의 연결되어 있는 컴퓨터 인덱스를 큐에 넣어주고
            #그 인덱스들을 갔다고 표시해준다.
            for index, j in enumerate(computers[i]):
                if check[index] == 0 and j == 1:
                    queue.append(index)
                    check[index] = 1

            ## 연결되어 있고 방문한적 없는 모든 컴퓨터들을 방문하고
            ## 그것들을 갔다고 표시해준다.
            while(len(queue) != 0):
                a = queue.pop(0)
                for index, j in enumerate(computers[a]):
                    if check[index] == 0 and j == 1:
                        queue.append(index)
                        check[index] = 1


    return(network)
                
            
                
            
                    
            
            
                



solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])

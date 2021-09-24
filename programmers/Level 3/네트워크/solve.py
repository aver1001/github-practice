def solution(n, computers):
    check = [0 for _ in range (n)]
    queue = []
    network = 0
    for i in range (n):
        if check[i] == 0:
            network += 1
            queue.append(i)
            while(len(queue) != 0):
                print(queue)
                index = queue.pop(0)
                if check[index] == 0:
                    for a,b in enumerate(computers[index]):
                        if check[a] == 0 and b == 1:
                            check[a] = 1
                            queue.append(a)
                        print(check)
            print('##')
    print(network)
                    
            
            
                



solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])

def solution(operations):
    queue = []
    for order in operations:
        #print(order[0],order[2:],queue)
        if order[0] == 'D' and len(queue) != 0:
            #최댓값 삭제
            if order[2:] == '1':
                queue.pop()
            ##최솟값 삭제
            elif order[2:] == '-1':
                queue.pop(0)
        elif order[0] == 'I':
            queue.append(int(order[2:]))
            queue.sort()
    
    if len(queue) == 0:
        return [0,0]
    else:
        return [queue[-1],queue[0]]

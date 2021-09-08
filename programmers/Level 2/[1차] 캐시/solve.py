def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    queue = []
    time = 0
    for i in cities:
        i = i.upper()
        print(queue,i,time)
        ## Hit
        if i in queue:
            print('Hit')
            queue.remove(i)
            queue.append(i)
            time += 1
        ## Miss
        else:
            if len(queue) == cacheSize:
                print('Miss')
                queue.pop(0)
                queue.append(i)
                time += 5
            else:
                print('Miss')
                queue.append(i)
                time += 5
    print(time)

solution(5,["SEOUL", "SEOUL", "SEOUL"] )

def solution(jobs):
    ready_queue = []
    time = 0
    endtime = 0
    pt = 0
    while (True):
        print(time)
        ##시간 맞춰서 작업 할 수 잇는 프로세스 레디큐로 이동
        while(len(jobs)!= pt):
            if jobs[pt][0] <= time:
                ready_queue.append(jobs[pt])
                pt += 1
            else:
                break
        print(ready_queue)
        ##레디큐 안에 있는 것 중에서 가장 빠르게 끝날 수 있는 것 파악

        if len(ready_queue) != 0 :
            Min = 9999
            for i in range (len(ready_queue)):
                print(ready_queue[i],ready_queue[i][1] - ready_queue[i][0])
                if Min > ready_queue[i][1] - ready_queue[i][0]:
                    print("Change")
                    Min = ready_queue[i][1] - ready_queue[i][0]
                    index = i

            come,runningTime = ready_queue.pop(index)
            time += runningTime
            endtime += time - come

        else:
            time += 1
        if len(ready_queue) == 0 and len(jobs) == pt:
            break
        
    print(time,endtime)
    print(endtime//len(jobs))
    
        
        
            
     
        

solution([[0, 3], [1, 9], [2, 6], [30, 3]])

def solution(jobs):
    jobs.sort()
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
        ##레디큐 안에 있는 것 중에서 가장 빠르게 끝날 수 있는 것 파악
        ready_queue.sort( key = lambda x: x[1])
        print(ready_queue)
        if len(ready_queue) != 0 :
            come,runningTime = ready_queue.pop(0)
            time += runningTime
            endtime += time - come

        else:
            time += 1
        if len(ready_queue) == 0 and len(jobs) == pt:
            break
        
    print(time,endtime)
    print(endtime//len(jobs))
    
        
        
            
     
        

solution([[0, 3], [1, 9], [2, 6], [30, 3]])

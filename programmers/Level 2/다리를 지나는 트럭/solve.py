def solution(bridge_length, weight, truck_weights):
    queue_weights = []
    queue_times = []
    times = 1
    #print(0,queue_weights,"   ",truck_weights)
    #print(' ',queue_times,'\n')
    while(truck_weights or queue_weights):
        
        if len(truck_weights) != 0:
            if sum(queue_weights)+truck_weights[0] <= weight:
                queue_weights.append(truck_weights.pop(0))
                queue_times.append(bridge_length)
    
            
            
        #print(times,queue_weights,"   ",truck_weights)
       # print(' ',queue_times,'\n')
        
        if len(queue_times) != 0:
            times += 1
            for i in range (len(queue_times)) : queue_times[i] -= 1
            if queue_times[0] == 0:
                queue_times.pop(0)
                queue_weights.pop(0)

    return times
        
            
        
            



bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length,weight,truck_weights))

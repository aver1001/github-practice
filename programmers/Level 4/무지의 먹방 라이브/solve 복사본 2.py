import heapq as hq

def solution(food_times, k):

    h = []
    N = len(food_times)

    
    ## [food_times,index]
    for i in range (N):
        hq.heappush(h,[food_times[i],i+1])

    time = 0
    hap = 0
    print(h)
    while h:

        ## 시간을 넘겨버렸을경우  
        if hap + (h[0][0] - time) * N > k:
            h.sort(key = lambda x:x[1])
            return h[(k-hap)%N][1]

        else:
            hap += (h[0][0] - time) * N
            time, _ = hq.heappop(h)
            N -= 1


    return -1
 




print(solution([3, 1, 2],5)) # 1 

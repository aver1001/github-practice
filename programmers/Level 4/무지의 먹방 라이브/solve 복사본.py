def solution(food_times, k):
    N = len(food_times)
    food_times = list(enumerate(food_times,start = 1))
    food_times.sort(key=lambda x:x[1])
    print(food_times)
    
    isEnd = [False for _ in range (N+1)]
    hap = 0
    Min = 0
    for i in range (N):
        if Min < food_times[i][1]:
            if k >= (hap + (food_times[i][1] - Min) * (N-i)):
                hap += (food_times[i][1] - Min) * (N-i)
                Min = food_times[i][1]
                isEnd[food_times[i][0]] = True
            else:
                break
        print(hap)
    else:
        print(-1)
            
    cnt = k - hap
    idx = 1
    print(cnt)
    print(isEnd)
    while cnt != 0 :
        if isEnd[idx] == False: cnt -= 1
        idx += 1
        print(idx)

    print(idx)
    




a = solution([3, 1, 2],5) # 1 

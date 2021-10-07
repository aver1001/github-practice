def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    answer = 0
    start, end = 1, distance 
    while start <= end:
        mid = (start + end) // 2
        
        # 부서진 바위의 수 세기
        cnt_rock = 0
        prev_rock = 0
        for rock in rocks:
            if rock - prev_rock < mid:
                cnt_rock += 1
            else:
                prev_rock = rock
            
        if cnt_rock > n:
            end = mid - 1
        else: 
            answer = mid
            start = mid + 1
            
    return answer
    


solution(25, [2, 14, 11, 21, 17], 2)

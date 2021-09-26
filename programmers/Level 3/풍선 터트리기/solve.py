def solution(a):
    answer = 0
    N = len(a)
    left_min = [0]*N
    right_min = [0]*N
    L_min = a[0]
    R_min = a[-1]
    
    for i in range(N):
        
        if L_min > a[i]:
            L_min = a[i]
        if R_min > a[N-1-i]:
            R_min = a[N-1-i]

        left_min[i] = L_min
        right_min[N-1-i] = R_min

    for i in range(N):
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1
    return(answer)

        


        
            
    

    
    

solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])
## return 6

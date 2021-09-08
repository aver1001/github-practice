def solution(land):
    hap = 0
    answer = []
    for i in range (1,len(land)):
        for j in range(4):
            Max = 0
            for k in range(4):
                if j!=k and Max < land[i-1][k]:
                    Max = land[i-1][k]
            land[i][j] = Max+land[i][j]
    return max(land[-1])

        



solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])

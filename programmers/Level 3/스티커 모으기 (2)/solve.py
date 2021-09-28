def solution(sticker):
    N = len(sticker)
    table1 = [0]*N
    table2 = [0]*N

    table1[0] = sticker[0]
    

    ## 첫 스티커 선택
    for i in range (1,N-1):
        table1[i] = max(table1[i-2]+sticker[i],table1[i-1])
    print(table1)

    for i in range (1,N):
        table2[i] = max(table2[i-2]+sticker[i],table2[i-1])
    print(table2)

    return max(table1[-2],table2[-1])




Q1 = [14, 6, 5, 11, 3, 9, 2, 10]    # 36
Q2 = [1, 3, 2, 5, 4]                # 8
Q3 = [1]

solution(Q3)

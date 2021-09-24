from collections import deque

def solution(enter, leave):
    ptE = 1
    ptL = 0
    N = len(leave)
    table = [0]*(N+1)
    answer = []
    while (True):
        ## 사무실 도착
        print(enter[:ptE])
        enter[:ptE]
        #만약 퇴근할사람이 있다면
        while(True):
            if leave[ptL] in enter[:ptE]:
                print("퇴근")
                ## 지금 있는 사람들 몇명인지 넣어줌
                table[leave[ptL]] += len(enter[:ptE-1])
                ## 퇴근시켜줌
                enter.remove(leave[ptL])
                ## 다음 퇴근할사람 가리킴
                ptL += 1
                ptE -= 1
                ## 남아있는 사람들은 퇴근한사람 마주쳤기 때문에 +1 씩해줌
                for i in enter[:ptE]:
                    table[i] += 1
                    
                if ptL == N:
                    return table
            else:
                break
        ptE += 1
    
    
    

print(solution([1,4,2,3],[2,1,3,4]))

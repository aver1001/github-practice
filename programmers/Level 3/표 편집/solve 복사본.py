from collections import deque

def solution(n, k, cmd):
    ## 행의 갯수 n
    ## 처음에 선택된 행의 위치 k
    ## 명령어들이 담긴 문자열 배열
    ## U X => X칸 위로
    ## D X => X칸 아래로
    ## C => 선택된 행을 삭제 후 바로 아래 행 선택 단 마지막 행일경우 삭제 후 자신의 위 인덱스를 선택
    ## Z => 최근에 삭제한 행을 복구, 단 선택된 행은 그대로
    
    answer = ['O' for _ in range (n)]
    pt = k
    backup = deque([])
    
    for cmd in cmd:
        ## U 명령어 
        if cmd[0] == 'U':
            move = int(cmd.split(' ')[-1])
            while(move != 0 ) :
                if answer[pt-1] == 'O':
                    move -=1
                pt -=1

        ## D 명령어
        elif cmd[0] == 'D':
            move = int(cmd.split(' ')[-1])
            while(move != 0) :
                if answer[pt+1] == 'O':
                    move -=1
                pt +=1

        ## C 명렁어
        elif cmd[0] == 'C':
            backup.append(pt)
            answer[pt] = 'X'
            while(answer[pt] != 'O' and pt != n-1):
                    pt += 1
            if pt == n-1 and answer[pt] == 'X':
                while(answer[pt] != 'O'):
                    pt -= 1
        ## Z 명령어
        elif cmd[0] == 'Z':
            answer[backup.popleft()] = 'O'
        #print(cmd,(' '*pt)+str(pt),''.join(answer) ,sep ='\n',end = '\n\n')
        
    return ''.join(answer)

print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))







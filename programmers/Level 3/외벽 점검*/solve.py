from collections import deque

def solution(n, weak, dist):

    ## 멀리갈 수 있는 친구 순으로 커버 가능한 양을 확인
    ## 취약 포인트에서 시작하도록 한다.
    dist.sort(reverse = True)
    table = {}
    for i in dist:table[i] = []

    ## 알고리즘 맞을 시 시간복잡도를 위해 이부분 수정 
    for move in dist:
        
        for s in weak:
            ##시계 방향
            point = []
            start = s
            for _ in range (move+1):
                if start in weak:
                    point.append(start)
                start += 1
                if start == n+1:
                    start = 1
            point.sort()
            if point != [] and point not in table[move]:table[move].append(point)
            start = s
            point = []
            ##반시계 방향
            for _ in range (move+1):
                if start in weak:
                    point.append(start)
                start -= 1
                if start == 0:
                    start = 12
            point.sort()
            if point != [] and point not in table[move]:table[move].append(point)

    cnt = 0
    queue2 = deque([[]])
    for i in table:
        print(i)
        cnt += 1
        course = table[i]
        print("table[i] :",course)
        queue = queue2.copy()
        while queue:
            
            temp = queue.popleft()
            print(temp)
            for i in course:
                ttemp = temp.copy()
                ttemp.extend(i)
                ttemp = set(ttemp)
                ttemp = list(ttemp)
                ttemp.sort()
                queue2.append(ttemp)
    return -1
            
            


a = solution(12,[1, 5, 6, 10],[1, 2, 3, 4])


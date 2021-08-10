import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while(scoville[0] <= K):
        print(scoville)
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        cnt+=1
        
    return cnt


scovile = [1, 2, 3, 9, 10, 12]

k = 7

print(solution(scovile,k))


'''
효율성 테스트에서 탈락. 
def solution(scoville, K):
    cnt = 0
    while(True):
        scovile.sort()
        #print(scovile)
        if scovile[0] >= K:
            break
        if len(scovile) == 1:
            return -1
        scovile.append(scovile.pop(0)+(scovile.pop(0)*2))
        cnt +=1
        
    return cnt
'''

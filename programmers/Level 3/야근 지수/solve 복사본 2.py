import heapq
def solution(n, works):
    
    heap = []

    for num in works:
      heapq.heappush(heap, (-num, num))

    while n != 0 :
        temp = heapq.heappop(heap)[1]-1
        heapq.heappush(heap,(-temp,temp))
        n -= 1
        
    answer = 0
    for a,b in heap:
        if b > 0:
            answer += b*b
    return answer
            

    

            
        



print((solution(13,[5,7,4,1,2])))

## 시간초과

from collections import deque

def solution(food_times, k):
    N = len(food_times)
    queue = deque(enumerate(food_times,start = 1))
    
    while queue:
        index,remain = queue.popleft()
        remain -= 1
        if remain != 0:
            queue.append([index,remain])
        k -= 1
        if k == 0: break
    index,remain = queue.popleft()
    return index


solution([3],5) # 1 

def solution(stones, k):
    
    N = len(stones)
    Min = 200000000
    for idx in range (N-k+1):
        if idx > Min:
            continue
        temp = max(stones[idx:idx+k])
        if Min > temp:
            Min = temp
            
    return Min

## 정확성 통과
## 효율성 실패 

def solution(stones, k):
    
    lt,rt = 1, 200000000
    while (lt < rt):
        pt = (lt+rt) // 2
        print(pt)
        temp = stones.copy()
        check = 0
        for stone in temp:
            if stone - pt <= 0:
                check += 1
            else:
                check = 0
                
            if check >= k:
                rt = pt
                break
        else:
            lt = pt+1
    return lt

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3)

## 정확성 통과
## 효율성 실패 

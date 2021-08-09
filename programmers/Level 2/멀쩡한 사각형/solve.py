import math
def solution(w,h):
    x = max(w,h)
    y = min(w,h)
    cnt = 0
    for i in range (1,x):
        if(i*y/x )% 1 != 0:
            cnt+=2
            
    return w*h-cnt

    return w


solution(12,8)

## 패턴을 찾아보려햇지만 실패.
## 기울기를 이용해서 풀려고 함.
# w = x  h = y 로 두고 생각햇을떄
# 기울기 * y 가 분수읽 ㅕ


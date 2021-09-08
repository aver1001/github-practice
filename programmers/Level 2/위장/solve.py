def solution(clothes):
    a = dict()
    for item, Class in clothes:
        if a.get(Class) == None:
            a[Class] = 1
        else:
            a[Class] = a[Class]+1
    answer = 1
    for i in list(a.values()):
        answer *= (i+1)

    return answer - 1
        
        
        
    



clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))

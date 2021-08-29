def solution(arr1, arr2):
    arr2 = [[element for element in t] for t in zip(*arr2)]
    answer = []
    for a in arr1:
        temp = []
        for b in arr2:
            res = 0
            for c,d in zip(a,b):
                res += c*d
            temp.append(res)
        answer.append(temp)
        
    return(answer)
    
            


solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]])

import itertools
import pandas as pd
def solution(relation):
    combiRelation = []
    ## 1
    for i in range(1,len(relation)):
        combiRelation.extend(map(list,itertools.combinations([0,1,2,3], i)))
    combiRelation = list(combiRelation)

    print(combiRelation)

    ## 2 이미 정렬 되어있음
    ## 3
    Candidate = []
    cnt = 0
    while(combiRelation):
        a = combiRelation.pop(0)
        temp2 = []
        for i in relation:
            temp = []
            for j in a:
                temp.append(i[j])
            if temp in temp2:
                break
            temp2.append(temp)
        if len(temp2) == len(relation):
            Candidate.append(a)
            for i in range (len(combiRelation)):
                b = combiRelation.pop(0)
                if a[0] in b:
                    continue
                else:
                    combiRelation.append(b)
                
    return len(Candidate)
            
                
                
            
            

relation = [["100","ryan","music","2"],["200","apeach","math","2"],
            ["300","tube","computer","3"],["400","con","computer","4"],
            ["500","muzi","music","3"],["600","apeach","music","2"]]
result = 2

a = solution(relation)

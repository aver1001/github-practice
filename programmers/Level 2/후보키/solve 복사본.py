def isCandidate(a,Candidate):
    for i in Candidate:
        if a & i == i:
            return False
    return True

def solution(relation):
    a = [a for a in range(1,len(relation)*len(relation)+1)]
    relationT = list(map(list,zip(*relation)))

    Candidate = []
    for i in a:
        print(bin(i))
        temp = []
        for j in range (len(relation)):
            if(i & (1 << j)) != 0:
                if len(temp) == 0:
                    temp = list(relationT[j])
                else:
                    temp = list(zip(temp,relationT[j]))
            print(temp)
        if len(set(temp)) == len(relation) and isCandidate(i,Candidate):
            Candidate.append(i)
    return(len(Candidate))



relation = [["100","ryan","music","2"],["200","apeach","math","2"],
            ["300","tube","computer","3"],["400","con","computer","4"],
            ["500","muzi","music","3"],["600","apeach","music","2"]]
result = 2
print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))

            

            




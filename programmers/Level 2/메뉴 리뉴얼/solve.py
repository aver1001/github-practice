from itertools import combinations

def solution(orders, course):
    result = dict()
    answer = []
    for i in orders:
        for j in range(2,len(i)+1):
            for k in list(combinations(list(i), j)):
                k = list(k)
                k.sort()
                res = ''.join(k)
                if len(k) in course:
                    if result.get(res) == None:
                        result[res] = 1
                    else :
                        result[res] = result[res]+1
    courseDict = dict()
    for i in course:
        courseDict[i] = 0
    for word in result.items():
        if courseDict.get(len(word[0])) < word[1] :
            courseDict[len(word[0])] = word[1]
    for word in result.items():
        if courseDict.get(len(word[0])) == word[1] and word[1] >= 2:
            answer.append(word[0])
    answer.sort()
    return answer
    


            
    


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
result = ["WX", "XY"]

print(solution(orders,course))

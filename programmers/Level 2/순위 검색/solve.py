from collections import defaultdict

def solution(info, query):
    group_info = defaultdict(list)
    for i, user_info in enumerate(info):
        lang, task, exp, food, score = user_info.split()
        score = int(score)
        
        case_list = []
        for a in ["-", lang]:
            for b in ["-", task]:
                for c in ["-", exp]:
                    for d in ["-", food]:
                        group_info[(a, b, c, d)].append(score)
            
    for key in group_info:
        group_info[key].sort()
    
    answer = []
    for q in query:
        lang, _, task, _, exp, _, food, score = q.split()
        score = int(score)
        
        temp = group_info[(lang, task, exp, food)]
        
        start, end = 0, len(temp) - 1
        while start <= end:
            mid = (start + end) // 2
            
            if temp[mid] < score:
                start = mid + 1
            else:
                end = mid - 1
            
        answer.append(len(temp) - start) 
    return answer





info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

a = solution(info,query)

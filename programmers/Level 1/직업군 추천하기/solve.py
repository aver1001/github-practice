def solution(table, languages, preference):
    answer = []
    Max = 0
    for i in table:
        i = i.split(' ')
        temp = 0
        for L,P in zip(languages,preference):
            try:
                temp += (6-i.index(L))*P
            except:
                continue
        print(i[0], ' : ', temp)
        if temp > Max:
            Max = temp
            answer = [i[0]]
        elif temp == Max:
            answer.append(i[0])
    answer.sort()
    return(answer[0])

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["PYTHON", "C++", "SQL"],[7, 5, 5])

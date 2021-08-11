import copy

def DFS(v,res,temp,operator):
    global Max
    if v == 3:
        operatorS = copy.deepcopy(operator)
        tempS = copy.deepcopy(temp)
        #print(res)
        for i in res:
            #print(i, end = ' => ')
            cnt = 0
            for j in range(len(operatorS)):
                #print(j,tempS)
                a = operatorS.pop(0)
                if a == i:
                    if a == '+':
                        tempS.insert(j- cnt,(tempS.pop(j- cnt) + tempS.pop(j- cnt)))
                    elif a == '-':
                        tempS.insert(j- cnt,(tempS.pop(j- cnt) - tempS.pop(j- cnt)))
                    elif a == '*':
                        tempS.insert(j- cnt,(tempS.pop(j- cnt) * tempS.pop(j- cnt)))
                    cnt +=1
                else:
                    operatorS.append(a)
        if abs(tempS[0]) >= Max:
            Max = abs(tempS[0])


    for i in ['+','-','*']:
        if i not in res:
            res.append(i)
            DFS(v+1,res,temp,operator)
            res.remove(i)
        

def solution(expression):
    temp = []
    operator = []
    lt, rt = 0, 0
    for i in range (len(expression)):
        ## 연산자 분리
        if expression[i].isdigit() == False:
            rt = i
            temp.append(int(expression[lt:rt]))
            operator.append(expression[i])
            lt = i+1

    
    temp.append(int(expression[lt:]))        
    #print(temp)
    #print(operator)
    global Max
    Max = 0

    DFS(0,[],temp,operator)
    return Max
    


expression = ["100-200*300-500+20","50*6-3*2"]
result = [60420,300]
solution(expression[1])

## 연산자가 뭐뭐 들었는지
## 정수, 연산자 분리..?

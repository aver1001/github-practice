def division(p):
    openP = 0
    closeP = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            openP += 1
        else:
            closeP += 1
        if openP == closeP:
            return p[:i + 1], p[i + 1:]
            

def isRight(p):
    cnt = 0
    for i in p:
        if i == '(': cnt += 1
        else: cnt -= 1
        if cnt < 0 : return False
    return True
        

def reverseBracket(p):
    result = ''
    for i in p[1:len(p)-1]:
        if i == '(':
            result += ')'
        else :
            result += '('
            
    return result

def solution(p):
    #1
    if p == '':
        return ''
    #2
    u,v= division(p)

    #3
    if isRight(u):
        # 3-1
        return u + solution(v)
    #4
    else:
        #4-1
        answer = '('
        #4-2
        answer += solution(v)
        #4-3
        answer += ')'
        #4-4
        answer += reverseBracket(u)
        #4-5
        return answer
        
        
    
    



P = ["(()())()",")(","()))((()"]
result = ["(()())()","()","()(())()"]
for i in range (3):
    print(solution(P[i]))

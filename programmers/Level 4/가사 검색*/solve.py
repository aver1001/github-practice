def findBefore(dic,str1):
    rindex = str1.rfind('?')
    lindex = str1.find('?')
    lenstr = len(str1)-1
        
    ## 오른쪽 ? 시작
    if rindex == lenstr and lindex != 0:
        cnt = rindex - lindex + 2
        for i in range (lindex-1,-1,-1):
            try:
                dic[str1[:i]+'?'*cnt]
                dic[str1] = [str1[:i]+'?'*cnt,0]
                return dic
            except:
                cnt+=1

    ## 왼쪽 ? 시작
    elif rindex != lenstr and lindex == 0:
        cnt = rindex - lindex + 2
        for i in range (rindex+1,len(str1)):
            try:
                dic[str1[:i]+'?'*cnt]
                dic[str1] = [str1[:i]+'?'*cnt,0]
                break
            except: 
                cnt += 1
            
    ## 모두 ? 일경우
    else:
        ## 최상위 노드이므로 찾을필요 없음
        dic[str1] = [None,0]
        
    return dic
    

def solution(words, queries):
    ## queries 를 순회하며 연결리스트로 이어줌
    ## table = { me : [before,cnt] }
    table = {q : [None,0] for q in queries}

    for q in queries:
        table = findBefore(table,q)

    print(table)

    for word in words:
        print(word)
        lenword = len(word)

        ## 오른쪽 시작
        MaxCheck = False
        
        for i in range (lenword-1,-1,-1):
            print(word[:i]+'?'*(lenword-i))
            try :
                table[word[:i]+'?'*(lenword-i)]
                str1 = word[:i]+'?'*(lenword-i)
                while (str1 != None):
                    
                    if str1 == '?'*lenword:
                        MaxCheck = True
                        
                    table[str1][1] += 1
                    str1 = table[str1][0]
                break
            except:
                continue
        print()
        ## 왼쪽 시작
        for i in range (1,lenword+1):
            print('?'*(i)+word[i:])
            try :
                table['?'*(i)+word[i:]]
                str1 = '?'*(i)+word[i:]
                while (str1 != None):
                    if MaxCheck and str1 == '?'*lenword:
                        break
                    table[str1][1] += 1
                    str1 = table[str1][0]
                break
            except:
                continue

    answer = []
    for a in queries:
        answer.append(table[a][1])

    print(answer)
            
        
        
    




'''
solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?",'?????','pro?'])
        ##Result [3, 2, 4, 1, 0]
'''
solution(["frodo", "frozz", "frozz", "frozen", "frame", "kakao"],
         ["fro??"])
        ## Result [3]

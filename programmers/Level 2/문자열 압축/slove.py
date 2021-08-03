def solution(s):
    
    list_s=list(s)
    print(list_s)
    for j in range (1,len(list_s)//2+1):
        result = ''
        cnt = 1
        temp = ''
        for i in range (0,len(list_s),j):
            print(temp, list_s[i:i+j])
            if temp == list_s[i:i+j]:
                cnt +=1
            else:
                if cnt == 1:
                    result += str.join('',list_s[i:i+j])
                else :
                    result = result + str(cnt) + str.join('',list_s[i:i+j])
                cnt = 1
            temp = list_s[i:i+j]
            print(result)
        print(result,len(result))
        print("#########################")
    answer = 0
    return answer





In = ["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]
'''
for i in In:
    solution(i)
'''
solution("ababcdcdababcdcd")
#

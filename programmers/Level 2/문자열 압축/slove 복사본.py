def solution(s):
    Min = 9999
    list_s=list(s)
    #print(list_s)
    for j in range (1,len(list_s)//2+1):
        #print("#########################",j)
        result = ''
        cnt = 1
        temp = list_s[0:]
        for i in range (0,len(list_s),j):
            #print(list_s[i:i+j],list_s[i+j:i+2*j])
            if list_s[i:i+j] == list_s[i+j:i+2*j]:
                cnt +=1
            else:
                if cnt == 1:
                    result += str.join('',list_s[i:i+j])
                else :
                    result = result + str(cnt) + str.join('',list_s[i:i+j])
                cnt = 1
            temp = list_s[i:i+j]
            #print(result)
        if len(result) < Min:
            Min = len(result)
       
    answer = Min
    return answer





In = ["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]
for i in In:
    print(solution(i))

#

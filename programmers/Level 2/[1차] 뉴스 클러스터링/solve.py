def J(A,B):
    if len(A) == 0 and len(B) == 0:
        return 65536
    else:
        return int(65536 * len(A) / len(B))

def solution(str1, str2):
    str1_L = []
    str2_L = []
    hap_L = []
    same_L = []
    ## 소문자 -> 대문자로 변경
    str1 = str1.upper()
    str2 = str2.upper()

    ## 2개씩 원소로 나누기 
    for i in range (len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_L.append(str1[i:i+2])

    for i in range (len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_L.append(str2[i:i+2])

    # 교집합 교집합 구하기
    for i in str1_L:
        if i in str2_L and i not in same_L:
            for j in range (min(str1_L.count(i),str2_L.count(i))):
                same_L.append(i)
        if i not in hap_L:
            for j in range (max(str1_L.count(i),str2_L.count(i))):
                hap_L.append(i)
    for i in str2_L:
        if i not in hap_L:
            for j in range (str2_L.count(i)):
                hap_L.append(i)     
 
    # 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력

    return J(same_L,hap_L)
    


str1 = 'FRANCE'
str2 = 'french'
print(solution(str1,str2))

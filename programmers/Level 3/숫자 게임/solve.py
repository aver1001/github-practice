def solution(A, B):
    A.sort()
    B.sort()
    N = len(A)
    apt=0
    bpt=0

    
    answer = 0
    while (apt != N and bpt != N):
        ## B팀이 더 클 경우
        print(A[apt],B[bpt])
        if A[apt] < B[bpt]:
            print('B득점')
            answer += 1
            apt += 1
            bpt += 1
        else :
            bpt += 1

    return answer


####################################
A = [5,1,3,7]

B = [2,2,6,8]


solution(A,B)



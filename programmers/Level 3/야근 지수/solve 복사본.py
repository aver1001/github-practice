'''
정확성 만점
효율성 50점

1씩 빼는것이 아닌 가장큰거를 두번쨰로 맞춰주면서 뺴야겠음.
'''


def solution(n, works):
    
    works.sort(reverse = True)
    N = len(works)
    pt = 0
    while (n > 0):
        for i in range (N-1):
            if works[-1] == 0:
                return 0
            if works[i] > works[i+1]:
                n -= works[i] - works[i+1]
                works[i] = works[i+1]
                print(works,n)
                break
        else:
            ## 다 같은숫자
            while(n > 0):
                for i in range(N):
                    works[i] -= 1
                    n -= 1
                    if n <= 0:
                        break
                    if works[-1] == 0:
                        return 0
                    print(works,n)

        

    print(works)
            
        



print(solution(13,[3,2,1]))

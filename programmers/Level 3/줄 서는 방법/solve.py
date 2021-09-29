def solution(n, k):
    print(k)
    factorial = [0]*(n)
    number = [i for i in range (1,n+1)]
    print(number)
    

    ## 일단 각 숫자의 자리별 몇개씩 들어가는지 팩토리얼로 구해놓음.
    for i in range (n):
        if i == 0:
            factorial[i] = 0
        elif i == 1:
            factorial[i] = 1
        else:
            factorial[i] = factorial[i-1]*i

    answer = []
    factorial.reverse()
    k -= 1
    
    for facto in factorial[:-1]:
        print(k)
        mok,na = divmod(k,facto)
        print(mok)
        answer.append(number.pop(mok))
        print()
        k = na
    
    answer.append(number.pop())
    print(answer)


solution(5,0)

def solution(numbers):
    answer = '' 
    numbers2 = [str(n)*3 for n in numbers] # 한줄 반복문을 통해 모든 원소들의 길이를 3 곱하여 새 배열 생성
    print(numbers2)
    numbers3 = list(enumerate(numbers2)) # 각 원소에 enumerate 함수로 인덱스 붙여줌
    print(numbers3)
    numbers3.sort(key = lambda x:x[1], reverse = True) # 원소들의 값에 따라 정렬
    for index, value in numbers3: # 정렬된 인덱스를 이용해 차례대로 answer 만들기
        answer += str(numbers[index])
        
    return str(int(answer))

def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))

numbers = [3, 30, 34, 5, 9]
answer = "6210"

print(solution2(numbers))




# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.


'''
시간초과
def solution(numbers):
    Max = 0
    for i in range (len(numbers)): numbers[i] = str(numbers[i])
    
    for i in list(permutations(numbers, len(numbers))):
        if Max < int(str.join('',i)):
            Max = int(str.join('',i))
    
    return str(Max)
'''

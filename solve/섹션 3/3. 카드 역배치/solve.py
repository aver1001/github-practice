'''
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓 여있다.
각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타낸다.
이제 여러분은 다음과 같은 규칙으로 카드의 위치를 바꾼다
구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.
예를 들어, 현재 카드가 놓인 순서가 위의 그림과 같고 구간이 [5, 10]으로 주어진다면,
위치 5부터 위치 10까지의 카드 5, 6, 7, 8, 9, 10을 역순으로 하여 10, 9, 8, 7, 6, 5로 놓는다.
오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면,
주어진 구간의 순서대로 위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤
마지막 카드들의 배치 를 구하는 프로그램을 작성하시오.

'''
import sys
import time


start = time.time()
for sn in range (1,6):
    sn = str(sn)
    input_file_name = 'in' + sn +'.txt'
    output_file_name = 'out' + sn +'.txt'
    
    sys.stdin = open (input_file_name, "rt",encoding = 'utf-8')
    output_file = open(output_file_name, "rt",encoding = 'utf-8')

#################################################################
    ## 입력 : 범위

    ## 20개의 카드 생성
    card = [i+1 for i in range(20)]

    
    ##범위 10개 불러오기
    for i in range (10):
        ai,bi = (map(int,input().split()))

        bot = card[:ai-1]
        mid= card[ai-1:bi]
        top = card[bi:]
        mid.reverse()
        card = bot + mid+top

    for i in card:
        print(i,end = ' ')
        
                

    
#################################################################
    
#################################################################
    print("\n"+output_file.read()+"\n####################\n")
end = time.time()
print('time elapsed', end - start)

    



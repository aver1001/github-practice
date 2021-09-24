

    


def hourTominute(time):
    
    if len(time) == 8:
        h,m,s = map(int,time.split(':'))
        return h*3600+m*60+s
    else:
        answer = []
        time = time.split('-')
        for i in time:
            h,m,s = map(int,i.split(':'))
            answer.append(h*3600+m*60+s)
        return answer

def minuteTohour(time):
    h = time // 3600
    m = (time - (h*3600)) // 60
    s = time % 60
    
    return str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2)

def solution(play_time, adv_time, logs):
    N = len(logs)+1
    logs.insert(0,'00:00:00-00:00:00')
    logs.sort()
    adv_time = hourTominute(adv_time)
    Max = 0
    for i in range (N):
        logs[i] = hourTominute(logs[i])
    for i in logs:
        for stand_A in i:
            stand_A= int(stand_A) 
            MarketShare = 0
            stand_B = stand_A + adv_time
        
            for a,b in logs:
                ## 광고시간에 포함 안될 경우
                if (b <= stand_A and b <= stand_B) or (a >= stand_A and a >=stand_B):
                    continue                
                ## 광고시간이 더 짧을 경우
                elif stand_A > a and stand_B < b:
                    MarketShare += adv_time
                ## 광고시간이 더 길 경우
                elif stand_A <= a and stand_B >= b:
                    MarketShare += b-a
                ## 왼쪽이 은 더 길고 오른쪽은 짧을 경우
                elif stand_A <= a and a < stand_B < b:
                    MarketShare += stand_B - a
                ## 왼쪽은 짧고 오른쪽은 길 경우
                elif a< stand_A < b and stand_B >= b:
                    MarketShare += b - stand_A
                    
                
            if MarketShare > Max:
                Max = MarketShare
                answer = stand_A

    return minuteTohour(answer)

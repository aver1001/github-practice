def Ispalindrome(str1):
    
    if str1 == '':
        return False
    slen = len(str1)//2+1
    
    for idx in range (slen):
        if str1[idx] != str1[-1-idx]:
            return False
        
    return True
    
def solution(s):
    N = len(s)
    Max = 0
    for lt in range (N):
        for rt in range (lt,N+1):
            if Ispalindrome(s[lt:rt]) and Max < len(s[lt:rt]):
                Max = len(s[lt:rt])
    return(Max)
                



solution("abcdcba") ## 7

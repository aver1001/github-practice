def solution(s):
    cnt = 0
    zero = 0
    while (s != '1'):
        zero += s.count('0')
        cnt += 1
        s = bin(s.count('1'))[2:]
    return([cnt,zero])


solution("110010101001")

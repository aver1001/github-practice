def DFS(word,v):
    global dic
    if v == 5:
        dic.add(word)
        return
    for i in ['','A', 'E', 'I', 'O', 'U']:
        DFS(word+i,v+1)
    

def solution(word):
    global dic
    dic = set()
    DFS('',0)
    dic = list(dic)
    dic.sort()
    return dic

a = solution('')

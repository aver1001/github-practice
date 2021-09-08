def solution(n, words):
    temp = set()
    temp.add(words[0])
    for index,word in enumerate(words[1:],start = 1):
        checkLen = len(temp)
        temp.add(word)
        if checkLen == len(temp) or (words[index-1])[-1] != word[0]:
            return [index % n+1,index // n+1]
    return [0,0]



print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

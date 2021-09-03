def solution(files):
    temp = []
    answer = []
    for order, name in enumerate(files):
        for index, i in enumerate(name):
            if i.isdigit():
                HEAD = index
                break
        for index, i in enumerate(name[HEAD:]):
            if i.isdigit() == False:
                NUMBER = index+HEAD
                break
        else:
            NUMBER = HEAD + index +1
        temp.append([name[0:HEAD].upper(),int(name[HEAD:NUMBER]),order,name])
    temp.sort(key = lambda x:x[2])
    temp.sort(key = lambda x:x[1],reverse = True)
    temp.sort()
    for i in temp : answer.append(i[3])
    return answer
        

a = solution(["img000012345", "img1.png","img2","IMG02"])

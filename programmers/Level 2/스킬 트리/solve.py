def solution(skill, skill_trees):
    cnt = 0
    for i in skill_trees:
        pt = 0
        for j in range (len(i)):
            if i[j] in skill:
                if i[j] == skill[pt]:
                    pt += 1
                else:
                    break
            if j == len(i)-1:
                cnt += 1
    
    return (cnt)


solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])

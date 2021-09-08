def solution(citations):
    citations.sort(reverse = True)
    for i in range (len(citations)):
        if i >= citations[i]:
            return i

    return len(citations)



citations = [6, 6, 6, 6, 6, 1]
print(solution(citations))

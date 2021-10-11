def solution(words, queries):
    answer = []
    counted = []
    
    for w in words:
        counted.append(len(w))

    print(counted)

    trie = make_trie({}, words)   # 조건 a 의 trie
    


def make_trie(trie, words):
    for word in words:
        cur = trie
        lens = len(word)
        for w in word:
            if w in cur:
                cur = cur[w]
                cur['!'].append(lens)
            else:
                cur[w] = {}
                cur = cur[w]
                cur['!'] = [lens]
    print(trie)
                    


def search_trie(trie, query, length):
    count = 0
    if query[0] == '?':
        return trie['!'].count(length)
    elif query[0] in trie:
        count += search_trie(trie[query[0]], query[1:], length)

    return count
        
        
    





a = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?",'?????','pro?'])
        ##Result [3, 2, 4, 1, 0]
'''
solution(["frodo", "frozz", "frozz", "frozen", "frame", "kakao"],
         ["fro??"])
        ## Result [3]
'''

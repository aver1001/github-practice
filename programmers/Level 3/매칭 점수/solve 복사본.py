def solution(word, pages):
    table = {}
    webpage = []
    word = word.upper()
    for first in pages:
        head = first.split('<head>\n')[1]
        head = head.split('\n</head>')[0]
        
        body = first.split('<body>\n')[1]
        body = body.split('\n</body>')[0]

        ##head 에서 URL 구하기
        thisurl = head.split('<meta property="og:url" content="')[1]
        thisurl = thisurl[:-3]
        if thisurl not in table:
            table[thisurl] = {'BaseScore':0,'OutUrl':0,'Mechoise':[]}
        webpage.append(thisurl)
        print(thisurl)
        ##body 에서 외부 URL 구하기
        ##body 에서 Basescore 구하기

        print('##########################')
        ## 이건 Url
        for text in (body.split('<a href="')):
            for ttext in text.split('"'):
                if ttext[:8] == 'https://':
                    if ttext not in table:
                        table[ttext] = {'BaseScore':0,'OutUrl':0,'Mechoise':[thisurl]}
                    else:
                        table[ttext]['Mechoise'].append(thisurl)
                    table[thisurl]['OutUrl'] += 1
                else:
                    ttext = ttext.upper()
                    print(ttext)
                    lt,rt = 0,1
                    for i in range (len(ttext)-1):
                        print(ttext[lt:rt])
                        if 65 <= ord(ttext[rt]) <= 90:
                            rt += 1
                        else:
                            if ttext[lt:rt] == word:
                                table[thisurl]['BaseScore'] += 1
                            lt = rt + 1
                            rt += 1
        print()
    Max = -5
    for idx,url in enumerate(webpage):
        print(url,'=>',table[url])
        temp = table[url]['BaseScore'] + sum([table[i]['BaseScore'] / table[i]['OutUrl']for i in table[url]['Mechoise']])
        if temp > Max:
            answer = idx
            Max = temp
    print(answer)

solution('Muzi',
         ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])

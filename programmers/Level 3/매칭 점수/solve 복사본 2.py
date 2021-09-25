import re

def solution(word, pages):
    
    table = {}
    target = []
    for page in pages:
        #print(page)
        ##URL 구하기
        thisurl = re.search('<meta property="og:url" content="(.+)"',page).group(1)
        ##외부 URL 구하기
        outurl = re.findall('<a href="(\S+)">',page)
        ##basescore 구하기
        basescore = re.sub('[^a-zA-z]',' ',page).lower().split().count(word.lower())
        #print("##########",thisurl,outurl,basescore,'##############')
        if thisurl not in table:
            table[thisurl] = {'BaseScore' : basescore,'Outurl':len(outurl),'Mechoise':[]}
        else:
            table[thisurl]['BaseScore'] = basescore
            table[thisurl]['Outurl'] = len(outurl)
            
        for i in outurl:
            if i not in table:
                table[i] = {'BaseScore' : 0,'Outurl':0,'Mechoise':[thisurl]}
            else:
                table[i]['Mechoise'].append(thisurl)
        target.append(thisurl)
        
    Max = -1
    for idx,url in enumerate(target):
        temp = table[url]['BaseScore'] + sum([table[i]['BaseScore'] / table[i]['Outurl']for i in table[url]['Mechoise']])
        #print(url,'=>',table[url],'=>',temp)
        if temp > Max:
            answer = idx
            Max = temp
    return(answer)



solution('Muzi',
         ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])

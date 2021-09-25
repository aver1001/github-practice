import random

cryptograph = ''
keyList = []
descrambling = ''

## 평문
plain = 'Do not try to be original, just try to be good.'
print('평문 : ',plain)

## 랜덤으로 키를 만들어 xor 하여 암호화 후 키 저장
for text in plain:
    key = random.randint(0,255)
    keyList.append(key)
    cryptograph += chr(ord(text) ^ ord(chr(key)))

## 변환된 암호문
print('암호화 : ',cryptograph)

## 암호문을 key와 xor하여 복호화 
for idx,text in enumerate(cryptograph):
    descrambling += chr(ord(text) ^ ord(chr(keyList[idx])))


##복호화 된 평문 
print('복호화 : ',descrambling)
    


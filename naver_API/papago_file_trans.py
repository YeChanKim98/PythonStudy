import os, sys
from pprint import pprint
import urllib.request
import json

client_id = "8aKjhWuBfvDwP1T1oyfb"
client_secret = "M1wTCcvfA9"

with open('test.txt', 'r', encoding='utf8') as f: # 인코딩은 선택사항
    srcText = f.read()

encText = urllib.parse.quote(srcText)
data = "source=ko&target=en&text=" + encText

url = "https://openapi.naver.com/v1/papago/n2mt"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    res = json.loads(response_body.decode('utf8')) # 리스트 방식으로 원하는 값을 추출하기 위해 Json으로 변환은 필수
    with open('translate.txt', 'w', encoding='utf8') as f:
        f.write(res['message']['result']['translatedText'])

else:
    print("Error Code:" + rescode)
import os, sys
from pprint import pprint
import urllib.request
import json

client_id = "8aKjhWuBfvDwP1T1oyfb"
client_secret = "M1wTCcvfA9"

encText = urllib.parse.quote("오늘의 파이썬 공부는 웹 활용")
data = "source=ko&target=ja&text=" + encText # 한국어에서 영어로 지정

url = "https://openapi.naver.com/v1/papago/n2mt"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # pprint(response_body.decode('utf-8'))
    data = json.loads(response_body) # 함수를 통해 json형식에 맞게 변수에 넣어준다
    pprint(data)

else:
    print("Error Code:" + rescode)
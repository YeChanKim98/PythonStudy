import os
import sys
import requests
from pprint import pprint
import json

# 개발자 센터에서 확인 후 기입
client_id = "8aKjhWuBfvDwP1T1oyfb"
client_secret = "M1wTCcvfA9"

url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
#url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

files = {'image': open('test01.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

response = requests.post(url,  files=files, headers=headers) # 얼굴인식에 대한 결과는 json형식으로 반환된다
# 웹에서 데이터나 객체를 문자로 표현하기 위한 방식이 json이다

rescode = response.status_code

if(rescode==200):
    #print (response.text)
    data = json.loads(response.text) # 함수를 통해 json형식에 맞게 변수에 넣어준다
    pprint(data)
    # pprint(data['faces'][0]['age']['value']) # 키를 이용한 세부사항 출력
    # pprint(type(data))

else:
    print("Error Code:" + rescode)
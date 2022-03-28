import re # 정규식 모듈
'''
# 정규 표현식 기초
# 정규 표현식은 기본적으로 []로 표현한다
# 표현식에 들어가는 .+*|^ 등의 문자를 메타문자라고 한다

# 정규식 기본 : 단순 문자 나열
[abc] # 보이는 그대로 a,b,c를 의미

# 정규식 기본 : From - To
[a-c] # a부터 c 즉, a,b,c를 의미
[0-5] # 0,1,2,3,4,5를 의미

# .(아무문자) : 줄바꿈(\n)을 제외한 모든 문자를 의미
[a.c] # abc, aac, a1c, 등 양 끝에 a와 c가 위치하고 가운데는 아무거나 있음을 의미
      # 단, acb는 당연히 불일치
      
# *(반복) : 앞에 나온 문자가 0번이상 있음을 의미
[ab*c] # ac, abbbc 가능

# +(반복) : 앞에 나온 문자가 1번이상 있음을 의미
[ab*c] # abc, abbbc 가능 단, ac는 불가능


# *이하 re.compile은 중괄호로 인해 컴파일 에러가 떠서 임시로 사용함

# {N}(지정반복) : 앞에나온 문자가 N번 반복됨을 의미
re.compile('[ab{3}c]') # abbbc 가능. 정확히 N번 반복되어야 함

# {M,N}(지정반복) : 앞에나온 문자가 M이상 N이하 반복됨을 의미
re.compile('[ab{1,3}c]') # abc, abbbbc 가능.

# ?(선택적) : 앞에나온 문자가 0번 혹은 1번 사용됨을 의미
re.compile('[ab?c]') # ac, abc 둘중 하나 가능

# ^(시작) : 뒤에나온 단어(문자)가 처음에 오는것을 의미
re.compile('^Hello') # Hello가 처음에 오는 문자열만 가능, HelloWorld

# $(끝): 뒤에나온 단어(문자)가 끝에 오는것을 의미
re.compile('Hello$') # Hello가 끝에 오는 문자열만 가능, World Hello
 
# \b(공백) : 해당 자리에 공백이 있음을 의미
re.compile('\band\b') # You and I 가 매칭됨 / UandI는 안 됨
 
# \s(띄어쓰기) : 앞 문자뒤에 띄어쓰기가 오는것을의미
# \w(단어) : 앞 문자뒤에 (아무)문자가 오는 것을 의미
re.compile('Hi\s\w+') # Hi뒤에 띄어쓰기가 있고, 아무 문자가 반복됨을의미(+를 넣어서 단어를 받게 할 수 있다 -> 띄어쓰기 전까지 인식 하므로)
# -> Hi User 가능 / Hi U s e r 를 할 경우 Hi U가 매칭

# r(이스케이핑) : 문자로 인식을 시키기위해서 백슬래스를 앞에 붙일 필요 없이 바로 적을 수 있다
re.compile(r'C:\\main') # \\을 일반 문자로 인식

# ()(그루핑) : 문자를 그룹으로 지정한다
re.compile('ABC+') # AB다음에 C가 한번이상 반복되는 것을 의미, 만약 ABC전체의 반복을 원하면 아래처럼 한다
re.compile('(ABC)+') # ABC를 묶은 후 +를 주어 ABC전체가 반복되는 것을 의미하도록 한다

# ?P<name> : 그룹핑된 문자열에 이름을 부여할 수 있다
re.compile('(?P<ABC>ABC)+') # group('ABC')를 통해서 불러올 수 있음

# (?=문자) (전방탐색 : 긍정형) : 지정한 문자까지 탐색조건에 포함되지만, 리턴되는 문자열에서는 제외된다
re.compile('.+(?=:)') # http://naver.com이라는 문자열이 있을 때, :의 앞인 http까지만 매칭된다

# (?=문자) (전방탐색 : 부정형) : 지정한 문자가 포함되지 않아야한다
# 지정한 확장자를 거를 때 유용
re.compile('.*[.](?!exe$)') # 아무문자가 다수 오고, 문자 '.'이 온 뒤 exe가 마지막에 오지 '않'는것을 매칭 
# 결과 exe라는 확장자를 거른다
'''

# 정규 표현식 실습

# Match : 완전히 식에 일치하지 않으면 None을 반환한다 / 처음 매칭된것이 있으면 종료
pattern = re.compile('[a-z]+') # a부터 z까지 1번이상 사용하여
match_res1 = pattern.match('apple') # True / 만약 Apple로 할 경우, False -> 대문자가 있으므로 매칭 안 됨
match_res2 = pattern.match('010-1234-5678') # False
print(match_res1,match_res2)

# Match객체의 메서드

# group : 지정한 그룹에 매칭된 결과를 반환, 만약 ()기호(그루핑기호)가 없으면 전체를 하나의 그룹으로 취급
match_res1 = pattern.match('apple_Banana_berry')
print('group-1',match_res1.group())

# start, end : 매치된 문자열의 시작, 끝 인덱스(위치)를 리턴

# span : 매치된 문자열의 (시작,끝)에 해당하는 튜플을 리턴
match_res1 = pattern.match('apple Banana berry').span()
print('span',match_res1)


# Search : 식에 일치하는 부분이 있으면 첫 일치 문자열에 대한 결과 반환한다
# 내장메서드 start, end를 통해서 문자의 몇번 인덱스부터 몇번 인덱스까지 일치하는지 확인이 가능하다
# 단 띄어쓰기를 기준으로 일치하는 첫 문자열만 반환
pattern = re.compile('[a-z]+') # a부터 z까지 1번이상 사용하여
search_res1 = pattern.search('apple Banana banana Apple') # True / 만약 Apple로 할 경우, False -> 대문자가 있으므로 매칭 안 됨
search_res2 = pattern.search('010-1234-5678') # False
print(search_res1, search_res2)

# 정규식과 문자를 동시에 인자로 넘길 수 있다
print(re.search('^Hello', 'Hello World'))

# FindAll : 식에 일치하는 모든 문자열에 대한 결과를 배열로 반환한다
# 일치하는 패턴이 없을경우, 빈 배열 반환
# finditer를 사용할 경우, 배열이아닌, 매칭 정보를 담은 이터레이터 오브젝트로 반환한다
pattern = re.compile('[a-z]+') # a부터 z까지 1번이상 사용하여
find_res1 = pattern.findall('Apple Banana') # True / 만약 Apple로 할 경우, False -> 대문자가 있으므로 매칭 안 됨
find_res2 = pattern.findall('010-1234-5678') # False
print(find_res1, find_res2)

# sub : 일치하는 패턴을 지정한 문자열로 치환한다
pattern = re.compile('(white|black|red|blue)')
pattern.sub('color', 'i could be black, i could be blue') # -> black과 blue가 color로 바뀐다

# 정규 표현식 옵션
pattern = re.compile('[a-z]',re.DOTALL) # 줄바꿈을 하나의 문자로 취급(혹은무시)하여 a.c가 a\nc를 매칭하게됨  /  re.s로 적어도 됨
pattern = re.compile('[a-z]',re.I) # 대소문자의 구분을 없앤다
pattern = re.compile('[a-z]',re.M) # 줄바꿈이 되더라도 모든 줄을 다 검색
pattern = re.compile(r""" #VERBOSE 옵션을 통해서 중간에 주석을 줄 수 있고 가독성이 올라간다
    &[#]  
    (
        0[0-7]+
        | [0-9]+
    )
    ;
    """, re.VERBOSE)
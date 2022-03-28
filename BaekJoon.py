import sys

def _1330_() :
    a1, a2 = input().split()
    a1 = int(a1)
    a2 = int(a2)
    res = '>' if a1 > a2 else '<' if a1 < a2 else '=='
    print(res)

def _9498_ () :
    score = int(input())

    if 100>=score>=90 :
        print('A')

    elif 89>=score>=80 :
        print('B')

    elif 79>=score>=70 :
        print('C')

    elif 69>=score>=60 :
        print('D')

    elif 59>=score>=0 :
        print('F')

def _2753_() :
    year = int(input())
    if(year%4 == 0 and ( year%400 == 0 or year%100 != 0 )) :
        print('1')
    else :
        print('0')

def _14681_() :
    Quadrant = [[3,2],[4,1]]
    x = 1 if int(input()) > 0 else 0
    y = 1 if int(input()) > 0 else 0
    print(Quadrant[x][y])

def _2884_() :
    h, m = map(int,input().split())
    if(m < 45) : # 45분보다 적어서 시가 바뀜
        print(23,15+m) if h==0 else print(h-1,15+m)
    else :
        print(h, m-45)

def _10950_():
    cnt = int(input())
    res=[]
    for a in range(cnt) :
        x, y = input().split()
        res.append(int(x)+int(y))
    for r in res :
        print(r)

def _10871_() :
    length, x = input().split()
    A = list(input().split())
    for i in A :
        if int(i) < int(x) : print(i)

def _1110_() :
    X = input()
    Original = '0'+X if len(X) < 2 else X
    cycle=0
    while True :
        if len(X) < 2 : X = '0'+X
        tmp = X[-1]+str(int(X[0])+int(X[1]))[-1]
        cycle+=1
        if Original==tmp :
            break
        else :
            X=tmp
    print(cycle)

def _10818_() :
    length = input()
    arr = input().split()
    max = int(arr[0])
    min = int(arr[0])
    for i in arr :
        if int(i) > max : max = int(i)
        if int(i) < min : min = int(i)
    print(min, max)

def _2577_() :
    cnt=[0,0,0,0,0,0,0,0,0,0]
    A = int(input())
    B = int(input())
    C = int(input())
    Res = str(A*B*C)
    for i in range(len(Res)) :
        cnt[int(Res[i])]+=1

    for i in cnt :
        print(i)

def _3052_() :
    cnt = list()
    arr = [int(input()) for i in range(10)]
    for i in arr :
        mod = i % 42
        if mod in cnt : pass
        else : cnt.append(mod)
    print(len(cnt))

def _1008_():
    a,b = input().split()
    print(int(a)/int(b))

def _2438_() :
    length = int(input())
    for i in range(length) :
        print('*'*(int(i)+1))

def _2562_() :
    arr = [int(input()) for i in range(9)]
    print(max(num_list))
    print(num_list.index(max(num_list)) + 1)

def _2675_() :
    cycle = int(input())
    res=list()
    for i in range(cycle) :
        tmp=''
        cnt, sen = input().split()
        for j in sen :
            tmp+=j*int(cnt)
        res.append(tmp)
    for a in res : print(a)

def _2739_() :
    a = int(input())
    for i in range(1,10) :
        print(a,'*',i,'=',a*i)

def _2920_() :
    a=['1','2','3','4','5','6','7','8']
    get = list(input().split())
    if a==get : print('ascending')
    elif list(reversed(a))==get : print('descending')
    else : print('mixed')

def _10869_() :
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a+b)
    print(a-b)
    print(a*b)
    print(int(a/b))
    print(a%b)

def _8958_() :
    cycle = int(input())
    for _ in range(cycle) :
        a = input()
        cost,total=0
        for i in a :
            if i=='O' : cost+=1
            else : cost=0
            total += cost
        print(total)

def _10951_() :
    while True :
        try :
            x, y = map(int, input().split())
            print(x+y)
        except :
            break

def _10952_() :
    while True :
        x, y = map(int, input().split())
        if x == 0 and y == 0 :
            break
        print(x+y)

def _11720_() :
    length = int(input())
    hap = 0
    a = input()
    for i in a :
        hap += int(i)
    print(hap)

def _11654_() :
    print(ord(input()))

def _1000_() :
    a,b = input().split()
    print(int(a)+int(b))

def _1152_() :
    a = input()
    cnt,chk=0,0
    for i in range(len(a)) :
        if a[i] != ' ' : chk=1
        if chk==1 and (a[i]==' ' or i==(len(a)-1)) : cnt+=1
    print(cnt)

def _1001_() :
    a,b = input().split()
    print(int(a)-int(b))

def _1157_() :
    sentence = input()
    res = dict()
    for i in sentence :
        i=i.lower()
        if i in res :
            res[i]+=1
        else :
            res[i]=1
    max_key = max(res, key=res.get)
    max_value = res.pop(max_key)
    if max_value in res.values() :
        print('?')
    else : print(max_key.upper())

def _1546_() :
    cycle = int(input())
    score = list(map(int,input().split()))
    max_score=max(score)
    total=0
    for i in score :
        total += int(i)/max_score*100
    print(total/cycle)

def _2439_() :
    size = int(input())
    for i in range(1,size+1) :
        print(' '*(size-i)+'*'*i)

def _2475_() :
    num = list(map(int,input().split()))
    hap = 0
    for i in num :
        hap += i**2
    print(hap%10)

def _2741_() :
    for i in range(int(input()),0,-1) :
        print(i)

def _2908_() :
    a,b = input().split()
    print(max(int(a[::-1]),int(b[::-1])))

def  _10171_() :
    print('\    /\\')
    print(' )  ( \')')
    print('(  /  )')
    print(' \(__)|')

def _10809_() :
    s = input()
    for i in range(97, 123) :
        if chr(i) in s :
            print(s.index(chr(i)),end=' ')
        else :
            print('-1',end=' ')
    # 인덱스 반환 없으면 -1 반환

def _10998_() :
    a,b=map(int,input().split())
    print(a*b)

def _1018_() :
    N, M = map(int, input().split())
    board = list()
    for i in range(N):
        board.append(input())
    repair = list()
    for i in range(N - 7):
        for j in range(M - 7):
            first_W = 0
            first_B = 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if (k + l) % 2 == 0:
                        if board[k][l] != 'W':
                            first_W = first_W + 1
                        if board[k][l] != 'B':
                            first_B = first_B + 1
                    else:
                        if board[k][l] != 'B':
                            first_W = first_W + 1
                        if board[k][l] != 'W':
                            first_B = first_B + 1
            repair.append(first_W)
            repair.append(first_B)

def _1085_() :
    x,y,w,h = map(int,input().split())
    print(min(x,y,(w-x),(h-y)))

def _1181_() :
    a=list()
    for _ in range(int(input())) :
        a.append(input())
    a=list(set(a))
    a.sort()
    a.sort(key=len)
    for i in a :
        print(i)

def _1259_() :
    while True :
        a = input()
        if a=='0' : break
        if a==''.join(reversed(a)) :
            print('yes')
        else : print('no')

def _10989_() :
    # 메모리 초과
    a = list()
    for i in range(int(input())) :
        a.append(int(input()))
    a.sort()
    for i in a : print(i)

    # input 사용으로 인한 메모리 초과 대응
    import sys
    n = int(sys.stdin.readline())
    b = [0] * 10001
    for i in range(n):
        b[int(sys.stdin.readline())] += 1
    for i in range(10001):
        if b[i] != 0:
            for j in range(b[i]):
                print(i)

def _4153_() :
    while True :
        a=list(map(int,input().split()))
        if max(a)==0 : break
        l=a.pop(a.index(max(a)))
        if l**2 == a[0]**2 + a[1]**2 :
            print('right')
        else : print('wrong')

def _10250_() :
    c=int(input())
    for i in range(c):
        h,w,a=map(int,input().split())
        y = str(a%h)
        x = int(a / h + 1)
        if y == '0' :
            y = str(h)
            x-=1
        if x < 10 :
            x='0'+str(x)
        print(y+str(x))

def _2231_() :
    a=int(input())
    for i in range(a) :
        hap = 0
        for j in str(i) :
            hap += int(j)
        if a == i+hap :
            print(i)
            break
        if i == a-1 :
            print(0)

def _2292_() :
    n = int(input())
    cnt = 1
    chk = 6
    res = 1
    while n > cnt:
        res += 1
        cnt += chk
        chk += 6
    print(res)

def _2775_() :
    t = int(input())
    for i in range(t):
        k = int(input())
        n = int(input())
        a = [x for x in range(1, n + 1)]
        for j in range(k):
            for y in range(1, n):
                a[y] += a[y - 1]
        print(a[-1])

def _2798_() :
    from itertools import combinations
    c,r=map(int,input().split())
    a=list(combinations(map(int,input().split()),3))
    h=0
    for i in a :
        if h<sum(i)<=r :
            h=sum(i)
    print(h)

def _15829_() :
    c,a=input(),input()
    hap = 0
    for i in range(len(a)) :
        hap+=(ord(a[i])-96)*(31**i)
    print(hap%1234567891)

def _2839_() :
    x,cnt=int(input()),0
    while x>0 :
        if x%5==0 :
            cnt+=int(x/5)
            x=0
            break
        else :
            x-=3
            cnt+=1
    print(cnt if x == 0 else -1)

def _2869_() :
    a,b,v=map(int,input().split())
    r=(v-a)//(a-b)+1
    print(r+1 if (v-a)%(a-b) > 0 else r)

def _11050_() :
    import math
    a,b=map(int,input().split())
    print(math.comb(a,b))

def _1436_() :
    n=int(input())
    cnt,a=0,666
    while True :
        if '666' in str(a) :
            cnt+=1
            if cnt == n :
                print(a)
                break
        a+=1

def _2609_() :
    from math import gcd,lcm
    a,b=map(int,input().split())
    print(gcd(a,b))
    print(lcm(a,b))

def _2751_() :
    # 시간 초과로 불가능
    # c=int(input())
    # a=[]
    # for i in range(c) :
    #     a.append(int(input()))
    # a=sorted(a)
    # for i in a :
    #     print(i)
    
    import sys
    c = int(sys.stdin.readline()) #  N(1 ≤ N ≤ 1,000,000)을 위해서 sys이용ㄴ
    n = []
    for i in range(c): n.append(int(sys.stdin.readline()))
    n = sorted(n)
    for i in range(c): print(n[i])

def _7568_() :
    a=int(input())
    d,c=[],[1 for i in range(a)]
    for _ in range(a) :
        d.append(list(map(int,input().split())))
    for i in range(len(d)) :
        for k in range(len(d)) :
            if d[i][0] < d[k][0] and d[i][1] < d[k][1] :
                c[i]+=1
    for i in c :
        print(i,end=' ')

def _10814_()  :
    # 시간 초과
    import sys
    c=int(sys.stdin.readline())
    d=[]
    for _ in range(c) :
        d.append(list(sys.stdin.readline().split()))
    p=0
    for i in range(c-1,-1,-1) :
        p = 0
        for j in range(i-1,-1,-1) :
            if d[i][0] < d[j][0] : p+=1
        if p > 0 :
            now=d.pop(i)
            target=d[i-p:]
            del d[i-p:]
            d.append(now)
            for i in target :
                d.append(i)
    for i in d :
        print(i[0],' ',i[1])

def _10814_2() :
    import sys
    c=int(sys.stdin.readline())
    d=[]
    for _ in range(c) :
        d.append(list(sys.stdin.readline().split()))
    res=[]
    for i in range(c) :
        res.append(d.pop(d.index(min(d))))
    for i in res :
        print(i)

def _10814_3() :
    import sys
    c=int(sys.stdin.readline())
    d=[]
    for _ in range(c) :
        d.append(list(sys.stdin.readline().split()))
    d.sort()
    for i in d :
        print(i[0],i[1])

def _10814_4() :
    import sys
    c = int(sys.stdin.readline())
    d = []
    for _ in range(c):
        d.append(list(sys.stdin.readline().split()))
    d.sort(key=lambda x: x[0])
    for i in d: print(*i, sep=" ")

def _10814_5() :
    import sys
    L = [[] for i in range(200)]
    for i in range(int(sys.stdin.readline())):
        a,b = sys.stdin.readline().split()
        L[int(a)-1].append(b)
    for i in range(200):
        for j in L[i]:
            print(i+1,j)

def _11650_() :
    import sys
    c=int(sys.stdin.readline())
    d=[]
    for i in range(c) :
        d.append(list(map(int,sys.stdin.readline().split())))
    d.sort(key=lambda x:(x[0],x[1]))
    for r in d :
        print(r[0],r[1])

def _11651_() :
    import sys
    c=int(sys.stdin.readline())
    d=[]
    for i in range(c) :
        d.append(list(map(int,sys.stdin.readline().split())))
    d.sort(key=lambda x:(x[1],x[0]))
    for r in d :
        print(r[0],r[1])

def _1920_() :
    from sys import stdin
    c1=stdin.readline()
    a1=set(map(int,stdin.readline().split()))
    c2=stdin.readline()
    a2=list(map(int,stdin.readline().split()))
    for a in a2 :
        if a in a1 :
            print('1')
        else :
            print('0')

def _1978_() :
    c=input()
    a=list(map(int,input().split()))
    cnt=0
    for i in a :
        flag=0
        if i == 1 :
            continue
        for j in range(2,i) :
            if i%j==0 :
                flag=1
                break
        if flag ==0 : cnt+=1
    print(cnt)

def _10828_() :
    from sys import stdin
    cycle = int(stdin.readline())
    stack=[]
    top = -1
    for _ in range(cycle) :
        command = list(stdin.readline().split())
        if command[0] == 'push' :
            stack.append(command[1])
            top+=1
        if command[0] == 'pop' :
            if top == -1 :
                print(-1)
            else :
                print(stack.pop(top))
                top-=1
        if command[0] == 'size' :
            print(len(stack))
        if command[0] == 'empty' :
            if top == -1 :
                print(1)
            else :
                print(0)
        if command[0] == 'top' :
            if top == -1 :
                print(-1)
            else :
                print(stack[top])

def _9012_() :
    cycle = int(input())
    for _ in range(cycle) :
        chk = 0
        bracket = input()
        for i in bracket :
            if i == '(' : chk+=1
            elif i == ')' : chk-=1
            if chk < 0 :
                break
        if chk != 0 :
            print('NO')
            continue
        print('YES')

def _10845_() :
    from sys import stdin
    cycle = int(stdin.readline())
    queue = []
    front,back = -1,-1
    for _ in range(cycle):
        command = list(stdin.readline().split())
        if command[0] == 'push':
            queue.append(command[1])
            back += 1
            if front < 0 :
                front += 1
        if command[0] == 'pop':
            if len(queue)==0:
                print(-1)
            else:
                print(queue.pop(0))
                front += 1
        if command[0] == 'size':
            print(len(queue))
        if command[0] == 'empty':
            if len(queue)==0:
                print(1)
            else:
                print(0)
        if command[0] == 'front':
            if len(queue)==0:
                print(-1)
            else:
                print(queue[0])
        if command[0] == 'back':
            if len(queue)==0:
                print(-1)
            else:
                print(queue[-1])

def _10866_() :
    from sys import stdin
    cycle = int(stdin.readline())
    dequeue = []
    front,back = -1,-1
    for _ in range(cycle):
        #print('dequeue :',dequeue,'/ front :',front,'/ back :',back)
        command = list(stdin.readline().split())
        if command[0] == 'push_back':
            dequeue.append(command[1])
            back += 1
            if front < 0 :
                front += 1
        if command[0] == 'push_front':
            dequeue.insert(0,command[1])
            back += 1
            if front < 0 :
                front += 1
        if command[0] == 'pop_front':
            if len(dequeue)==0:
                print(-1)
            else:
                print(dequeue.pop(0))
                front += 1
        if command[0] == 'pop_back':
            if len(dequeue) == 0:
                print(-1)
            else:
                print(dequeue.pop(-1))
                back -= 1
        if command[0] == 'size':
            print(len(dequeue))
        if command[0] == 'empty':
            if len(dequeue)==0:
                print(1)
            else:
                print(0)
        if command[0] == 'front':
            if len(dequeue)==0:
                print(-1)
            else:
                print(dequeue[0])
        if command[0] == 'back':
            if len(dequeue)==0:
                print(-1)
            else:
                print(dequeue[-1])

def _2164_() :
    from sys import stdin
    card = [x for x in range(int(stdin.readline()),0,-1)]
    for _ in range(len(card)-1) :
        card.pop()
        card.insert(0,card[-1])
        card.pop()
    print(card[0])

def _2164_2() :
    # 규칙을 찾아서 식을 만들면 시간 단축 가능
    from collections import deque
    N = int(input())
    deque = deque([i for i in range(1, N + 1)])
    while (len(deque) > 1):
        deque.popleft()
        move_num = deque.popleft()
        deque.append(move_num)
    print(deque[0])

def _11866_() :
    N,K=map(int,input().split())
    num=[x for x in range(1,N+1)]
    order,point=[],1
    while len(order) != N :
        if point%K==0 :
            order.append(num[(point%len(num))-1] if point > len(num) else num[point-1])
            if point > len(num) :
                num[point%len(num)-1]=-1
            else : num[point-1]=-1
        print('point :', point, ' ', num, ' --> ', order)
        point+=1
    print(order)

def _11866_2() :
    from collections import deque
    n, k = map(int, input().split())
    s = deque([i for i in range(1, n + 1)])
    print('<', end='')
    while s:
        for i in range(k - 1):
            s.append(s[0])
            s.popleft()
        print(s.popleft(), end='')
        if s:
            print(', ', end='')
    print('>')

def _10773_() :
    from sys import stdin
    c,h = int(stdin.readline()),0
    stack=[]
    for _ in range(c) :
        a=int(stdin.readline())
        if a == 0 :
            h-=stack[len(stack)-1]
            del stack[len(stack)-1]
        else :
            h+=a
            stack.append(a)
    print(h)



# 1주차 : 재귀함수, 누적합, 구현

def _3986_() :
    c=int(input())
    word,cnt=[],0
    for _ in range(c) :
        word.append(input())
    for i in word :
        stack=[]
        for j in i :
            if stack == []:
                stack.append(j)
            else :
                if stack[-1] == j :
                    del stack[-1]
                else :
                    stack.append(j)
        if stack == [] :
            cnt+=1
    print(cnt)

def _1213_() :
    from itertools import permutations
    import math
    from sys import stdin
    a=stdin.readline().strip()
    r=[]
    for i in a :
        r.append(i)
    c=set(r) #permutations(r,len(r)))
    r.clear()
    for i in c :
        front = list(i[:math.floor(len(i)/2)])
        back = list(i[math.ceil(len(i)/2):])
        back=back[::-1]
        if front == back :
            r.append(i)
    r.sort()
    if r!=[] :
        print(''.join(r[0]))
    else :
        print('I\'m Sorry Hansoo')

def _1213_2() :
    a=list(input())
    cnt,table=0,[]
    for i in range(65,91) :
        table.append(a.count(chr(i)))
    for i in table :
        if i%2==1 : cnt +=1
    if cnt > 1 :
        print('I\'m Sorry Hansoo')
    else :
        front,middle='',''
        for  i in range(len(table)) :
            if table[i]>1:
                front+=str(chr(i+65)*(int(table[i]/2)))
            if table[i]%2!=0:
                middle = chr(i + 65)
        print(front+middle+front[::-1])

def _1620_() :
    from sys import stdin
    d,c=map(int,stdin.readline().split())
    Poketmon={}
    for i in range(d) :
        Poketmon[i+1]=stdin.readline().strip()
    for i in range(c) :
        q = stdin.readline().strip()
        if q.isdigit() :
            print(Poketmon[int(q)])
        else :
            for key, value in Poketmon.items():
                if q == value:
                    print(key)

def _1620_2() :
    import sys
    d,c=map(int,sys.stdin.readline().split())
    p1,p2={},[]
    for i in range(d) :
        name = sys.stdin.readline().strip()
        p1[name]=i+1
        p2.append(name)
    for i in range(c) :
        q = sys.stdin.readline().strip()
        if q.isdigit() :
            print(p2[int(q)-1])
        else :
            print(p1[q]) # list의 인덱스 찾기를 이용하면 너무 느림 -> dict과 병행하는 것이 코드는 더러우나 이득

def _2309_() :
    k=[]
    for _ in range(9) :
        k.append(int(input()))
    k.sort()
    hap,b=sum(k),False
    for i in range(len(k)-1) :
        for j in range(1,len(k)) :
            if hap - (k[i]+k[j]) == 100 :
                k1,k2=k[i],k[j]
                k.remove(k1)
                k.remove(k2)
                b=True
            if b : break
        if b: break
    for i in k :
        print(i)

def _10808_() :
    a=list(input())
    table=[]
    for i in range(97,123) :
        table.append(a.count(chr(i)))
    print(' '.join(map(str,table)))

def _2979_() :
    p = list(map(int,input().split())) # 낼 돈
    s,e,cnt = 100,0,0
    pay=0
    t=[]
    for _ in range(3) : # 트럭의 각 주차 시간
        t.append(list(map(int,input().split())))
    for i in range(3) : # 도착 및 출발 시간 범위 지정
        if t[i][0] < s :
            s = t[i][0]
        if t[i][1] > e :
            e = t[i][1]
    for i in range(s,e+1) :
        cnt=0
        if t[0][0] <= i < t[0][1] :
            cnt+=1
        if t[1][0] <= i < t[1][1] :
            cnt+=1
        if t[2][0] <= i < t[2][1] :
            cnt+=1
        pay+=cnt*p[cnt-1]
    print(pay)

def _10988_() :
    a = input()
    p = int( len(a) / 2 )
    front = a[:p]
    back = a[p:] if len(a) % 2 == 0 else a[p+1:]
    if front==back[::-1] :
        print('1')
    else :
        print('0')

def _1159_()  :
    c=int(input())
    name=[]
    cnt=[0 for _ in range(26)]
    for _ in range(c) :
        name.append(input())
    for i in name :
        cnt[ord(i[0])-97]+=1
    res=''
    for i in range(26) :
        if cnt[i] > 4 :
            res+=chr(i+97)
    if res!='' :
        print(res)
    else :
        print('PREDAJA')

def _11655_() :
    s = input()
    res = ''
    for i in range(len(s)) :
        c = ord(s[i]) #
        if 96 < c < 123 : # 소문자
            if c+13 > 122 :
                res += chr(96+(c+13)%122)
            else :
                res += chr(c+13)
        elif 64 < c < 91 : # 대문자
            if c + 13 > 90:
                res += chr(64 + (c + 13) % 90)
            else:
                res += chr(c + 13)
        else :
            res+=s[i]
    print(res)

def _9996_() :
    c = int(input())
    s,e = input().split('*')
    for _ in range(c):
        w = input()
        if w[:len(s)] == s and w[-len(e):] == e and len(s)+len(e) <= len(w):
            print("DA")
        else:
            print("NE")

def _2559_() :
    from sys import stdin
    d,s = map(int,stdin.readline().split())
    t = list(map(int,stdin.readline().split()))
    m = 0
    c = 0
    for i in range(d-s) :
        for j in range(i,i+s) :
            c += t[j]
        m = c if c > m else m
    print(m)

def _2559_2() :
    d,s = map(int,input().split())
    t = list(map(int,input().split()))
    start, end, hap = 0,s-1,sum(t[:s]) # i / i+s-1
    max = hap
    print(hap)
    for i in range(1,d-s) :
        start += 1
        end += 1
        hap = hap-t[start-1]+t[end]
        max = hap if hap > max else max
        print('i=',i,' / start=',start,' / end=',end,' / hap=',hap,' / max=',max)
    print(max)

def _2559_3() :
    d,s = map(int,input().split())
    t = list(map(int,input().split()))
    ini = sum(t[:s])
    hap = [ini]
    for i in range(1,d-s) :
        ini = ini-t[i-1]+t[i+s-1] # -1 로 인해서 1개 연속을 조건으로 걸면 맨 마지막은 확인하지 않음 : 제거
        hap.append(ini)
    print(max(hap))

def _2559_4() :
    N, K = map(int, input().split())
    tem_list = list(map(int, input().split()))
    part_sum = sum(tem_list[:K])
    result_list = [part_sum]
    for i in range(0, len(tem_list) - K):
        part_sum = part_sum - tem_list[i] + tem_list[i + K]
        result_list.append(part_sum)
    print(max(result_list))

def _1940_() :
    N = int(input()) # 재료수
    M = int(input()) # 맞춰야하는 수
    num = sorted(list(map(int,input().split())))
    cnt = 0
    for i in range(N-1) :
        if num[i] >= M :
            break
        for j in range(i+1,N) :
            if num[i] + num[j] >= M :
                break
            if num[i] + num[j] == M :
                print(num[i],' / ',num[j],' --> 조합 가능')
                cnt += 1
    print(cnt)

def _1940_2() :
    N = input() # 재료수
    M = int(input()) # 맞춰야하는 수
    num = sorted(list(map(int,input().split()))) # [1,2,3,4,5,7]
    cnt = 0
    for i in num :
        if M-i in num and M-i != i:
            num.remove(i)
            num.remove(M-i)
            cnt+=1
    print(cnt)

def _1940_3() :
    N = int(input())# 재료수
    M = int(input()) # 맞춰야하는 수
    m = sorted(list(map(int,input().split()))) # [1,2,3,4,5,7]
    f,b,cnt = 0,N-1,0
    while f < b :
        h = m[f]+m[b]
        if h==M :
            cnt+=1
            f+=1
            b-=1
        elif h>M :
            b-=1
        else :
            f+=1
    print(cnt)

def _9375_() : # X
    c = int(input()) # 전체 Cycle
    N = int(input()) # 총 옷 수
    Closet={} # 옷 종류, 옷 이름
    k = []
    for _ in range(N) :
        name, kind = input().split()
        if kind not in Closet :
            k.append(kind)
            Closet[kind]=[name]
        else :
            Closet[kind].append(name)

    cnt = 0
    for i in range(2,len(k)-1) :
        for j in range(i+1,len(k)) :
            pass

def _9375_2() :
    from collections import Counter
    for i in range(int(input())):
        comb = 1
        kind = [] # 종류 리스트
        for j in range(int(input())):
            kind.append(input().split()[1]) # 종류 입력
        cnt = Counter(kind)
        for i in cnt:
            comb *= cnt[i] + 1
        print(comb-1)

def _1629_() :
    a,b,c = map(int,input().split())
    print(a*b%c)

def _4375_() : # 시간 초과
    N = int(input())
    p=N
    while True :
        if str(N).count('1') == len(str(N)) :
           print(len(str(N)))
           break
        else :
           N=int(N)+p

def _4375_2() :
    while True :
        try :
            N = int(input())
            p='1'
            while True :
                if int(p)%N == 0 :
                   print(len(p))
                   break
                else :
                   p+='1'
        except EOFError:
            break

def _1629_() :
    a, b, c = map(int, input().split())

    def recursive(a, n):
        if n == 1:
            return a
        return recursive(a, n - 1) * a

    print(recursive(a, b) % c)

def _1629_2() :
    a,b,c = map(int,input().split())
    def recursive(a, n):
        if n == 1:
            return a%c
        x = recursive(a, n//2)
        if n % 2 == 0:
            return x * x % c
        else:
            return x * x * a % c

    print(recursive(a,b))
# 1주차 끝

def _10816_() :
    c1 = input()
    d=dict()
    for i in map(int,input().split()) :
        # collection 모듈 안에 있는 defaultdict(int)를 이용하면 기본값이 항상 0으로 잡히기에 조건 없이 바로 +=1 을 할 수 있다
        d[i]= d[i]+1 if i in d else 1

    c2 = input()
    for i in map(int,input().split()) :
        print(d[i], end=' ') if i in d else print('0',end=' ')

def _10816_2() :
    from sys import stdin
    c1 = stdin.readline()
    q1 = sorted(list(map(int,stdin.readline().split())))
    c2 = stdin.readline()
    q2 = list(map(int,stdin.readline().split()))
    d={q1[0]:1}
    for i in range(1,len(q1)) :
        if q1[i] == q1[i-1] :
            d[q1[i]]+=1
        else :
            d[q1[i]]=1
    for i in q2 :
        try:
            print(d[i], end=' ')
        except KeyError :
            print('0',end=' ')
            
# 에라토스테네스의 체
def prime_list(n): 
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def _1929_() :
    s,e = map(int,input().split())
    arr=[True]*(e+1)
    arr[0]=arr[1]=False
    for i in range(2,int(e**0.5)+1) :
        if arr[i] :
            for j in range(i*i,e+1,i) :
                arr[j]=False

    for i in range(s,e+1) :
        if arr[i] :
            print(i)

# 분할 정복 알고리즘 :이분 탐색(이진 탐색)
def binary_search() :
    s,e = map(int,input().split())
    arr = [x for x in range(s,e+1)]
    s,e = 0,len(arr)-1
    num = int(input())
    flag=False

    while s <= e :
        m = (s+e+1)//2
        if arr[m] == num :
            flag=True
            break
        elif arr[m] < num :
            s = m+1
        else  :
            e = m-1

    print(flag)

def _2108_() : # 시간초과 ◟(`ﮧ´ ◟ )
    from sys import stdin
    from collections import Counter
    c = int(stdin.readline())
    num = []
    for _ in range(c) :
        num.append(int(stdin.readline()))
    num.sort()
    print(round(sum(num)/c))
    print(num[c//2])

    # 최빈값 : 가장 많이 나타나는 값
    cnt = Counter(num).most_common()
    if len(cnt) > 1 :
        print(cnt[1][0]) if cnt[0][1] == cnt[1][1] else print(cnt[0][0])
    else : print(cnt[0][0])
    # cnt = sorted(cnt.items(), key = lambda x : (-x[-1], x[0])) # 다중 키 정렬

    print(num[-1]-num[0])

def _4949_() :
    # A rope may form )(a trail in a maze.
    # ([(([([])()(( ))]))]).
    # 괄호를 확인하여 스택에 저장
    # 닫는 괄호가 오면 가장 위의 괄호와 비교 후 pop 만약 짝이 않맞으면 break 후 NO출력
    while True :
        p = input()
        flag=1
        s = []
        if p == '.' :break # .이 오면 종료

        for i in p :
            if i == '(' or i == '[' :
                s.append(i)
            if i == ')' :
                if len(s) == 0 :
                    flag = 0
                    break
                if s[-1] =='(' : del s[-1]
                else :
                    flag = 0
                    break
            if i == ']' :
                if len(s) == 0 :
                    flag = 0
                    break
                if s[-1] == '[': del s[-1]
                else :
                    flag = 0
                    break
        if flag == 1 and len(s)==0 : print('yes')
        else : print('no')

# 이분 탐색
def _2085_() : # pypy3 는 통과이지만 Python3는 시간초과

    # 0. 값 받기 : 나무수 / 필요 값 / 나무 배열
    # 1. 정렬 : 오름
    # 2. 첫 값과 마지막 값을 더한 후 //2 값으로 자른다
    # 3. 자른 값이 요구 값보다 크다면 왼쪽으로 작다면 오른쪽으로 반복한다
    # 4. 값을 찾으면 답
    
    N, M = map(int,input().split())
    Tree = list(map(int,input().split()))
    l,r=0,max(Tree)
    while l<r :
        point = (l + r) // 2+1
        hap = sum([max(0,i-point) for i in Tree])
        if hap >= M :
            l = point
        elif hap < M :
            r = point-1
    print(l)

    # sort와 순수for를 이용한 작성 : 시간초과
    # N, M = map(int, input().split())
    # Tree = list(map(int, input().split()))
    # l, r = 0, max(Tree)
    # point = (l + r) // 2
    # hap = 0
    # while hap != M:
    #     hap = 0
    #     for i in Tree:
    #         if i < point: continue
    #         hap = hap + (i - point)
    #     if hap > M:
    #         l = point
    #     elif hap < M:
    #         r = point
    #     point = (l + r) // 2
    #     if hap == M:
    #         break
    # print(point)

def _1966_() : # 복습
    from collections import deque
    for _ in range(int(input())) :
        N, M = map(int, input().split())
        p = list(map(int,input().split()))
        q = deque((i,x) for i,x in enumerate(p))
        p.sort()
        cnt=0
        while q :
            i,x = q.popleft()
            if x == p[-1] :
                p.pop()
                cnt+=1
                if i == M :
                    print(cnt)
                    break
            else :
                q.append((i,x))

def _1874_() :
    c = int(input()) # 받을 숫자 갯수
    stack,arr,res=[],[],[] # 검사할 수열 / 계산에 사용할 스택 / 결과
    cnt, stack_index = 1, 0 # 숫자카운터 / 수열의 위치를 지정할 인덱스

    for _ in range(c) :
        stack.append(int(input()))

    # 초기 설정
    res.append('+')
    arr.append(cnt)

    while cnt != c : # 증가
        if len(arr) != 0 : # 안에 요소가 있으면 판단 후 푸시 혹은 팝
            if stack[stack_index] == arr[-1] :
                stack_index += 1
                res.append('-')
                arr.pop()

            else: # 일치하지 않으면 입력
                cnt += 1
                res.append('+')
                arr.append(cnt)
        else : # 요소 없으면 입력
            cnt += 1
            res.append('+')
            arr.append(cnt)

    while stack_index < c : # 감소
        cnt -= 1
        if stack[stack_index] < arr[-1] :
            res.clear()
            res.append('NO')
            break
        elif stack[stack_index] == arr[-1] :
            stack_index += 1
            res.append('-')
            arr.pop()

    for i in res :
        print(i)

def _1874_2() :
    import sys
    n = int(sys.stdin.readline())
    stack = []
    result = []
    cnt = 0
    for _ in range(n):
        num = int(sys.stdin.readline())
        while cnt < num:
            cnt += 1
            stack.append(cnt)
            result.append("+")

        if stack[-1] == num:
            stack.pop()
            result.append("-")
        else:
            print("NO")
            break
    else:
        for x in result:
            print(x)

def _1654_() :
    K, N = map(int,input().split()) # 현재 랜선 수 / 필요 랜선 수
    Lan=[]
    for _ in range(K) :
        Lan.append(int(input()))
    l,h=1,max(Lan)
    while l < h :
        m = (l+h)//2+1
        cnt = sum([i//m for i in Lan])
        if cnt >= N :
            l = m
        else :
            h = m - 1
    print(l)

# 포기..
def _18111_() :
    from collections import defaultdict
    Block = defaultdict(int)
    N,M,B = map(int,input().split()) # 세로, 가로, 인벤토리 속 블럭 수
    time_cnt = 0 # 시간 계산
    for _ in range(N) :
        for i in list(map(int,input().split())) :
            Block[i]+=1

    Block = dict(sorted(Block.items(),key=lambda x : x[1],reverse=True))
    print('입력 받은 블럭 :',Block)
    # print(Block.values())
    # if 1 in list(Block.values()) : print("CHECK!!")
    while True : # M*N not in list(Block.values()) :
        value_arr = list(Block.values())
        if sum(value_arr[:-1]) <= B :
            print(value_arr)
            p = value_arr[0]
            for i in Block :
                if Block[i]!=p :
                    print(max(Block))
                    print(i)
                    print(Block[i])
                    time_cnt += (max(Block)-i)*Block[i]*2
                    print('Time_cnt : ',time_cnt)
            break
        else :
            tmp = Block[max(Block)]
            Block[max(Block)-1]+=tmp
            del(Block[max(Block)-1])
            time_cnt +=tmp*2
            B+=tmp
            print('블록 부족으로 인한 조정')
            print('  -> Block :',Block)
            print('  -> vlaue_arr :',Block.values())



    # for문을 통해서 최고층에서 최저층까지 내려오면서 확인한다
    # 현재 기준층에서 위로는 제거 후 인벤토리/시간 연산 후 아래를 채우는데 필요한 블록/시간을 계산한다
    # 만약 채우기 위한 블록이 부족하면 넘어간다
    # 블록이 충분하면 계산된 소요시간과 층을 출력한다


def _18111_2() :
    from sys import stdin
    from collections import Counter

    input = stdin.readline

    def minecraft(g, b):
        gg = Counter(g)
        ret = []  # (시간, 땅의 높이)
                    # 깍는게 시간이 더 많이 걸리니까 깍는걸 더 적게하는 높은 곳부터 시작
                    # 땅의 높이가 가장 높은곳에서 낮은 곳으로
        for h in range(max(gg.keys()), -1, -1):
            gt = 0
            inventory = b
            needed = 0
            for gh, gc in gg.items():
                if h < gh: # 지정 높이(h)보다 높은 곳은 깍아서 인벤토리로
                    inventory += (gh - h) * gc
                    gt += 2 * (gh - h) * gc
                elif h > gh: # 지정 높이(h)보다 낮은 곳은 갯수 확인
                    needed += (h - gh) * gc
                    gt += (h - gh) * gc
            if inventory >= needed: # 지정된 높이(h)보다 작은 곳을 채울 블록이 있는지 확인
                ret.append([gt, h])
            # 없으면 한칸 내려감
        ret.sort(key=lambda x: (x[0], -x[1]))
        return ret[0]


    if __name__ == "__main__" :
        N, M, B = map(int, input().split())
        grounds = []
        for _ in range(N):
            grounds.extend(list(map(int, input().split())))
        res = minecraft(grounds, B)
        print(res[0], res[1])

def _11723_() :
    from sys import stdin
    s = set()
    for _ in range(int(stdin.readline())) :
        k = list(stdin.readline().split())

        if len(k) == 1 :
            if k[0] == 'all' :
                s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
            else :
                s.clear()
        else :
            k[1]=int(k[1])

            if k[0] == 'add' :
                s.add(k[1])

            elif k[0] == 'remove':
                s.discard(k[1])

            elif  k[0] == 'check' :
                print(1 if k[1] in s else 0)

            elif k[0] == 'toggle' :
                try :
                    s.remove(k[1])
                except KeyError :
                    s.add(k[1])

def _1676_() :
    c = int(input())
    z = c//5+c//25+c//125
    print(z)

def _1764_() :
    N,M = map(int,input().split())
    d,b = set(),set()

    for _ in range(N) :
        d.add(input())
    for _ in range(M) :
        b.add(input())

    res = sorted(d & b)
    print(len(res))
    for i in res :
        print(i)

def _1107_() : # 리모콘
    channel,push_num = 100,0 # 기본 채널 초기화, 누른 횟수
    target = input() # 목표 채널
    M = int(input()) # 망가진 버튼 수
    remote = [0,1,2,3,4,5,6,7,8,9] # 리모컨
    push='' # 현재 누른 버튼

    # 리모컨 망가진 버튼 받기
    mal = list(map(int,input().split()))
    for i in mal :
        remote.remove(i)

    for i in range(len(target)) : 
        if target[i] in remote : # 버튼이 멀쩡하면
            push_num+=1 # 누름
            push+=str(i) # 버튼 추가
        else : # 없으면 가까운 값을 누른다
            pass



# _1107_()





a = int(input())
if a % 4 == 0 and ( a % 100 != 0 or a % 400 == 0) : print('Yes')
else : print('No')
#
# print *
# 괄호
#
#














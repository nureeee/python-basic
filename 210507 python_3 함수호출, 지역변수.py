'''
def Disp(name = '만수르'):
    print(name, '님은 돈이 많아요..')

Disp()
Disp('전용진')

def Disp2(x):
    for i in x:
        print(i)

def Disp3(x):
    print(x, id(x))    ##a, b의 id값과 같다.
    
def Disp4(*x):     ##리스트의 개별 값이 튜플형태로 전달
    for i in x:
        print(i, end = '  ')
'''

## 빌트인 함수명은 허용되나, 사용하면 안된다.

'''

def SUM(x):
    s = 0
    for i in x:
        s = s+i
    return s    #리턴이 없으면 값이 나오지 않는다.

def SUM1(*x):
    s = 0
    for i in x:
        s = s+i
    return s
    

a = [3, 6, 9]


b = a
Disp2(a)
Disp3(a)
# 에러 Disp3(*a)
print(id(a), id(b))
Disp4(*a)

print(SUM(a))
print(SUM([1, 2, 3, 4, 5, 6]))
print(SUM1(*a)

'''

'''

color = {'black':'검정', 'yellow':'노랑', 'blue':'파랑'}  #사전형 데이터

def disp_color(**x):  #**x의 **는 사전형 데이터를 받는다는 의미
    for key, value in x.items():
        print(key, value)
    print(x['black'], x['yellow'], x['blue'])

disp_color(**color)

'''

'''

gg=500

def f1(x):
    global gg  ## 전역변수 gg를 뜻함, 변수를 밖에서 찾아서 사용하여 값이 2이 된다.
    gg = 2
    print(gg, ' x ==> ', x*x)

def f2(x, y):
    t = x*y    ## t는 지역변수, f2함수 내에서만 통용된다
    print(gg, t)

f1(10)
print('  gg ==>  ', gg)
f2(100, 300)
print('  gg ==>  ', gg)

'''
## 파이써은 모든 것을 객체로 취급한다.
## 정수, 실수, 리스트, 함수, 클래스...











        

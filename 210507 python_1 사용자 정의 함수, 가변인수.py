## 사용자 정의 함수
'''

def f1():  ### 함수 정의
    pass   ###아무 일도 하지 않움

def f2():
    print(' f2...')
    
def f3(x):
    print(x, '가 좋아요')

def f4(x, y):
    print('{} + {} = {}'.format(x, y, x+y))
    
def plus(x, y):
    return x-y


f1()  ###함수 호출
f2()
print (f3(3))
f3(3)
f4(100, 23)
retv = plus(23, 4)
print(retv)
print ('23 - 4 =', plus(23, 4))

'''

'''
##덧셈만 할 수 있는 게산기

def f4(x, y):
    #print('{} + {} = {}'.format(x, y, x+y))
    return x+y

def f5(x, y):
    return x+y

while True:
    number1 = int(input('첫 번째 수 : '))
    if number1 == 0:
        break
    number2 = int(input('두 번째 수 : '))

    f4(number1, number2)
    
    print('{} + {} = {}'.format(number1, number2, number1 + number2))

    retv = f5(number1, number2)
    print('{} + {} = {}'.format(number1, number2, retv))

'''
'''
def Talk(x, y):
    print(x, '님이', y, '번 말씀하셨다.')

def Aha(x):
    print(x, '. 누구나 딱 한 번 산다고')


print(' start ')

name = input('이름 : ')
num = int(input('횟수 : '))

for i in range(1, num+1): 
    Aha(i)

Talk(name, num)  ##함수 호출

print(' End ')

'''

'''
##초간단 계산기

def Add(x, y):
    return x+y

def Sub(x, y):
    return x-y

def Mul(x, y):
    return x*y

def Div(x, y):
    return x//y

while True:
    print(' ** 간단한 계산기 **')
    n1 = int(input(' 첫 번째 수 : '))
    if n1 == 0:
        break
    
    
    op = input('[+, -, *, /] : ')
        
    n2 = int(input(' 두 번째 수 : '))
    

    if op == '+':
        res = Add(n1, n2)
    elif op == '-':
        res = Sub(n1, n2)
    elif op == '*':
        res = Mul(n1, n2)
    elif op == '/':
        res = Div(n1, n2)
    else:
        print(op, '없는 연산입니다.')
    print('{} {} {} = {}'.format(n1, op, n2, res))

'''
## 가변인수 ( 개수가 달라질 수 있다. + 여러개 대입도 처리가 가능하다.)

def Add(x =100, y=100, z=100):
    '''나는 값을 더하는 함수다.'''
    print('x = ', x, 'y = ', y, 'z = ', z)

    

def Call(x = '철수'):
    print(x, '야! 놀자')

Call()
Call('누리')
Add()
Add(10)
Add(y=10, x=5, z=5)



























 


















































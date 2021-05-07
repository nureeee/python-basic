'''
def f1():
    pass

def f2():
    print(' f2...')

def f3(x):
    print(x, '가 좋아요.')

def f4(x, y):
    print('{} + {} = {}'.format(x, y, x+y))

def plus(x, y):
    return x-y

f1()
f2()
f3(8)
f4(5, 2)
plus(4, 6)
retv = plus(5, 6)
print(retv)
print('23 - 4 =', plus(23,4))

'''

'''

def f1(x,y):
    #print('{} + {} = {}'.format(x, y, x+y))
    return x+y

def f2(x, y):
    return x+y

while True:
    number1 = int(input('첫 번째 수 : '))
    if number1 == 0:
        break
    number2 = int(input('두 번째 수 : '))

    #f1(number1, number2)
    #print('{} + {} = {}'.format(number1, number2, number1+number2))

    retv = f2(number1, number2)
    print('{} + {} = {}'.format(number1, number2, retv))

'''
'''

def Talk(x, y):
    print(x, '님이', y, '번 말슴하셨다.')

def Aha(x):
    print(x, '. 누구나 딱 한 번 산다고')

print('start')

name = input('이름 : ')
num = int(input('횟수 : '))

for i in range(1, num+1):
    Aha(i)

Talk(name, num)

print(' End ')

'''
def Add(x, y):
    return x+y

def Sub(x, y):
    return x-y

def Mul(x, y):
    return x*y

def Div(x, y):
    return x//y

while True:
    print('  ** 간단한 계산기 **')
    n1 = int(input('  첫 번째 수 : '))
    if n1 == 0:
        break

    op = input('[+, -, *, /]: ')

    n2 = int(input('두 번째 수 : '))


    if op == '+':
        res = Add(n1, n2)
    elif op == '-':
        res = Sub(n1, n2)
    elif op == '*':
        res = Mul(n1, n2)
        elif op == '/':
        res = Div(n1, n2)
    else:
        print(op,'없는 연산입니다.')
      print('{} {} {} = {}'.format(n1, op, n2, res))
        
'''

def Add(x = 100, y=100, z = 100):
    print('x= ', x, 'y= ', y, 'z= ', z)



def Call(x = '철수'):
    print(x, '야! 놀자')

Call()
Call('누리')
Add()
Add(10)
Add(y=10, x=5, z=5)
        
    


    

























































    
    

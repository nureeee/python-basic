Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    int(a)
NameError: name 'a' is not defined
>>> a = 100
>>> int(a)
100
>>> int(a)+100
200
>>> a = int(input())

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: ''
>>> a = int(input())
400
>>> a
400
>>> a= int(input('정수입력: '))
정수입력: 500
>>> city= input('어디서 오셨나요: ')
어디서 오셨나요: 부산시
>>> city
'부산시'
>>> a
500
>>> a= float(input('실수입력: '))
실수입력: 20.22
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
20.22
>>> print(a, city)
20.22 부산시
>>> 
>>> 
>>> print('aa \t bb \t cc \n dd \t ee \a ff \b gg')
aa 	 bb 	 cc 
 dd 	 ee  ff  gg
>>> print('서울은 좁아요' "아주 좁아요""정말 좁아요")
서울은 좁아요아주 좁아요정말 좁아요
>>> print('서울은 좁아요'\t "아주 좁아요"\n"정말 좁아요")
SyntaxError: unexpected character after line continuation character
>>> print('서울은 좁아요\t' "아주 좁아요\n""정말 좁아요")
서울은 좁아요	아주 좁아요
정말 좁아요
>>> age =20
>>> name = '빌게이츠'
>>> print(name '님은' age'살')
SyntaxError: invalid syntax
>>> print(name, '님은', age, '살')
빌게이츠 님은 20 살
>>> print('%s, %d ' %(name, age))
빌게이츠, 20 
>>> 
>>> print('%s, %d ' %(name, age))
빌게이츠, 20 
>>> int(agr)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(agr)
NameError: name 'agr' is not defined
>>> int(age)
20
>>> print('[%d] [%10d] [%-10d]' %(5, 5, 5))
[5] [         5] [5         ]
>>> print('{} {}'.format(10, 'seoul'))
10 seoul
>>> print('{} {} {}'.format(10, 3.14, 'seoul'))
10 3.14 seoul
>>> print('{\n} {\n} {\n}'.format(10, 3.14, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print('{\n} {\n} {\n}'.format(10, 3.14, 'seoul'))
KeyError: '\n'
>>> print('{}\n {} {}'.format(10, 3.14, 'seoul'))
10
 3.14 seoul
>>> print('{}\n{}\n{}'.format(10, 3.14, 'seoul'))
10
3.14
seoul
>>> print('{}\n{}\n{0}'.format(10, 3.14, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print('{}\n{}\n{0}'.format(10, 3.14, 'seoul'))
ValueError: cannot switch from automatic field numbering to manual field specification
>>> print('{0}\n{0}\n{0}'.format(10, 3.14, 'seoul'))
10
10
10
>>> 'print('[{0}]\n[{0}]\n{0}'.format(10, 3.14, 'seoul'))
SyntaxError: unexpected character after line continuation character
>>> 'print('[{0}]\n[{0}]\n[{0}]'.format(10, 3.14, 'seoul'))
SyntaxError: unexpected character after line continuation character
>>> 'print(' [{0}] [{0}] [{0}] '.format(10, 3.14, 'seoul')
SyntaxError: invalid syntax
>>> 'print('[{0}] [{0}] [{0}]'.format(10, 3.14, 'seoul')
SyntaxError: invalid syntax
>>> print('[{0}] [{0}] [{0}]'.format(10, 3.14, 'seoul
				 
SyntaxError: EOL while scanning string literal
>>> print('[{0}] [{0}] [{0}]'.format(10, 3.14, 's
				 
SyntaxError: EOL while scanning string literal
>>> print('[{0}]\n[{0}]\n{0}'.format(10, 3.14, 'seoul'))
[10]
[10]
10
>>> print('[{:20}]\n[{:-10}]\n{:10}'.format(10, 3.14, 'seoul'))
[                  10]
[      3.14]
seoul     
>>> print('[{:<20}]\n[{:<-10}]\n{:<10}'.format(10, 3.14, 'seoul'))
[10                  ]
[3.14      ]
seoul     
>>> print('[{^20}]\n[{:^10}]\n{:<10}'.format(10, 3.14, 'seoul'))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print('[{^20}]\n[{:^10}]\n{:<10}'.format(10, 3.14, 'seoul'))
KeyError: '^20'
>>> print('[{:^20}]\n[{:^10}]\n{:<10}'.format(10, 3.14, 'seoul'))
[         10         ]
[   3.14   ]
seoul     
>>> print('[{:^20}]\n[{:2f}]\n{:<10}'.format(10, 3.14, 'seoul'))
[         10         ]
[3.140000]
seoul     
>>> print('[{:^20}]\n[{:2f}]\n{:<10}'.format(10, 3.14, 'seoul'))
[         10         ]
[3.140000]
seoul     
>>> print('[{:^20}]\n[{:.2f}]\n{:<10}'.format(10, 3.14, 'seoul'))
[         10         ]
[3.14]
seoul     
>>> print('[{:^20}]\n[{:.3f}]\n{:<10}'.format(10, 3.14, 'seoul'))
[         10         ]
[3.140]
seoul     
>>> print('[{:^20}]\n[{:.10f}]\n{:<10}'.format(10, 3.14, 'seoul'))
[         10         ]
[3.1400000000]
seoul     
>>> print('[{:^20}]\n[{:10f}]\n{:<10}'.format(10, 3.14, 'seoul'))
[         10         ]
[  3.140000]
seoul     
>>> print('%f, %.f, %2f, %.10f'.format(2.13, 2.13, 2.13, 2.13))
%f, %.f, %2f, %.10f
>>> print('{%f}, {%.f}, {%2f}, {%.10f}'.format(2.13, 2.13, 2.13, 2.13))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print('{%f}, {%.f}, {%2f}, {%.10f}'.format(2.13, 2.13, 2.13, 2.13))
KeyError: '%f'
>>> print('{%f}, {%.f}, {%2f}, {%.10f}'.format(2.13, 2.13, 2.13, 2.13))print('%f, %.f, %2f, %.10f'.format(2.13, 2.13, 2.13, 2.13))
SyntaxError: invalid syntax
>>> print('%f, %.f, %2f, %.10f'.format(2.13, 2.13, 2.13, 2.13))print('{:%f}, {:%.f}, {:%2f}, {:%.10f}'.format(2.13, 2.13, 2.13, 2.13))
SyntaxError: invalid syntax
>>> print('%f, %.f, %2f, %.10f' %(2.13, 2.13, 2.13, 2.13))
2.130000, 2, 2.130000, 2.1300000000
>>> 
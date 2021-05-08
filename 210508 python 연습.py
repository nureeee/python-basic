Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pow
<built-in function pow>
>>> pow(2,3)
8
>>> pow(3,4)
81
>>> 2**2
4
>>> pow(2,34)
17179869184
>>> import math as m
>>> m.pi
3.141592653589793
>>> m.pi
3.141592653589793
>>> m.cos(10)
-0.8390715290764524
>>> m.tan(10)
0.6483608274590866
>>> m.log(100,2)
6.643856189774725
>>> a = 10
>>> a
10
>>> hex(a)
'0xa'
>>> oct(a)
'0o12'
>>> bin(a)
'0b1010'
>>> a
10
>>> print("16진수 : ", hex(a), "8진수 : ", oct(a), "2진수 : ")
16진수 :  0xa 8진수 :  0o12 2진수 : 
>>> b = int(input("정수 입력 : "))
정수 입력 : 3
>>> b = int(input("정수 입력 : "))
정수 입력 : 5.4
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b = int(input("정수 입력 : "))
ValueError: invalid literal for int() with base 10: '5.4'
>>> print("%f" %(k))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print("%f" %(k))
NameError: name 'k' is not defined
>>> k = 5.15 - 5.05
>>> k
0.10000000000000053
>>> print(" %f " %(k))
 0.100000 
>>> print(" %.20f " %(k))
 0.10000000000000053291 
>>> print(" %.2f " %(k))
 0.10 
>>> print(" %.15f " %(k))
 0.100000000000001 
>>> 1.7+1.7
3.4
>>> sum = 0.0
>>> for i im range(100):
	
SyntaxError: invalid syntax
>>> for i in range(100):
	Sum = Sum + 1.7

	
Traceback (most recent call last):
  File "<pyshell#33>", line 2, in <module>
    Sum = Sum + 1.7
NameError: name 'Sum' is not defined
>>> for i in range(100):
	Sum = Sum + 1.7

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    Sum = Sum + 1.7
NameError: name 'Sum' is not defined
>>> Sum = 0.0
>>> for i in range(100):
	Sum = Sum + 1.7

	
>>> 
>>> print(Sum)
169.99999999999986
>>> print("%.15" %(Sum))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print("%.15" %(Sum))
ValueError: incomplete format
>>> print("%.15f" %(Sum))
169.999999999999858
>>> 'T'.isalpha()
True
>>> bc4 = "kbs:mbc:sbs"
>>> bc4
'kbs:mbc:sbs'
>>> bc5 = bc4.split()
>>> bc5
['kbs:mbc:sbs']
>>> for i in a:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    for i in a:
TypeError: 'int' object is not iterable
>>> for i in a:
print(i)
SyntaxError: expected an indented block
>>> for i in b:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    for i in b:
TypeError: 'int' object is not iterable
>>> for i in range(3):
	print(i)

	
0
1
2
>>> a = 1
>>> a.encode()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.encode()
AttributeError: 'int' object has no attribute 'encode'
>>> while True:
	c = input("한 문자 입역 : ")
	if c == '0':
		break
	print(c, "==>", ord(c))

	
한 문자 입역 : 4
4 ==> 52
한 문자 입역 : 
Traceback (most recent call last):
  File "<pyshell#64>", line 5, in <module>
    print(c, "==>", ord(c))
TypeError: ord() expected a character, but string of length 0 found
>>> 
>>> for i in range(65, 91):
	print(i, "==>", chr(i))

	
65 ==> A
66 ==> B
67 ==> C
68 ==> D
69 ==> E
70 ==> F
71 ==> G
72 ==> H
73 ==> I
74 ==> J
75 ==> K
76 ==> L
77 ==> M
78 ==> N
79 ==> O
80 ==> P
81 ==> Q
82 ==> R
83 ==> S
84 ==> T
85 ==> U
86 ==> V
87 ==> W
88 ==> X
89 ==> Y
90 ==> Z
>>> k = [ chr(i) for i in range(65, 91)]
>>> k
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
>>> len(k)
26
>>> k[0]
'A'
>>> for i in k:
	print(i)

	
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
>>> for i in k:
	print(i, end = '')

	
ABCDEFGHIJKLMNOPQRSTUVWXYZ
>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
>>> type(a)
<class 'list'>
>>> len(a)
3
>>> a[0]
1
>>> a.append(2)
>>> 
>>> a
[1, 2, 3, 2]
>>> a.append(4)
>>> a[6][0]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a[6][0]
IndexError: list index out of range
>>> a[2][0]
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a[2][0]
TypeError: 'int' object is not subscriptable
>>> a.append([88,99])
>>> a
[1, 2, 3, 2, 4, [88, 99]]
>>> a[5][0]
88
>>> a.pop()
[88, 99]
>>> a.append([88,99])
>>> t = a.pop()
>>> t
[88, 99]
>>> t.insert (0, 3)
>>> t
[3, 88, 99]
>>> a.append(t)
>>> a
[1, 2, 3, 2, 4, [3, 88, 99]]
>>> a[3]
2
>>> a[:3]
[1, 2, 3]
>>> a = {'이름' : '김철수', '나이' : 30, '직업': '학생'}
>>> a['이름']
'김철수'
>>> a.items()
dict_items([('이름', '김철수'), ('나이', 30), ('직업', '학생')])
>>> a.keys()
dict_keys(['이름', '나이', '직업'])
>>> a.values()
dict_values(['김철수', 30, '학생'])
>>> for i, j in a.items():
	print(i, j)

	
이름 김철수
나이 30
직업 학생
>>> for key, value in a.items():
	print(key, "-->", val)

	
Traceback (most recent call last):
  File "<pyshell#116>", line 2, in <module>
    print(key, "-->", val)
NameError: name 'val' is not defined
>>> for key, value in a.items():
	print(key, "-->", value)

	
이름 --> 김철수
나이 --> 30
직업 --> 학생
>>> print(a)
{'이름': '김철수', '나이': 30, '직업': '학생'}
>>> a.update({4 : 'four'})
>>> a
{'이름': '김철수', '나이': 30, '직업': '학생', 4: 'four'}
>>> a.popitem()
(4, 'four')
>>> a
{'이름': '김철수', '나이': 30, '직업': '학생'}
>>> a.clear
<built-in method clear of dict object at 0x00000258F3FF8440>
>>> a
{'이름': '김철수', '나이': 30, '직업': '학생'}
>>> a.clear()
>>> 
>>> a
{}
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> for i in range(5):
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in range(5):
	print (i)

	
0
1
2
3
4
>>> for i in 1, 2, 3:
	print(i)

	
1
2
3
>>> for nation in '대한민국', '일본', '중국':
	print(nation, end = '  ')

	
대한민국  일본  중국  
>>> for i in range(1, 10):
	print ("{} * {} = {}".format(5, i, 5*i))

	
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
>>> dan = int(input(" 몇 단 출력할까요 : "))
 몇 단 출력할까요 : 1
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
 몇 단 출력할까요 : 
	 dan = int(input(" 몇 단 출력할까요 : "))
Traceback (most recent call last):
  File "C:/Users/82102/Desktop/파이썬/210508 python 노트.py", line 1, in <module>
    dan = int(input(" 몇 단 출력할까요 : "))
ValueError: invalid literal for int() with base 10: ''
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
 몇 단 출력할까요 : 3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
 몇 단 출력할까요 : 8
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
 몇 단 출력할까요 : 0
 프로그램 종료 
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
 sum = 55
>>> sum = 0
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
 i =>  1, sum =>   1
 i =>  2, sum =>   3
 i =>  3, sum =>   6
 i =>  4, sum =>  10
 i =>  5, sum =>  15
 i =>  6, sum =>  21
 i =>  7, sum =>  28
 i =>  8, sum =>  36
 i =>  9, sum =>  45
 i => 10, sum =>  55
 i => 11, sum =>  66
 i => 12, sum =>  78
 i => 13, sum =>  91
 i => 14, sum => 105
 i => 15, sum => 120
 i => 16, sum => 136
 i => 17, sum => 153
 i => 18, sum => 171
 i => 19, sum => 190
 i => 20, sum => 210
 i => 21, sum => 231
 i => 22, sum => 253
 i => 23, sum => 276
 i => 24, sum => 300
 i => 25, sum => 325
 i => 26, sum => 351
 i => 27, sum => 378
 i => 28, sum => 406
 i => 29, sum => 435
 i => 30, sum => 465
 i => 31, sum => 496
 i => 32, sum => 528
 i => 33, sum => 561
 i => 34, sum => 595
 i => 35, sum => 630
 i => 36, sum => 666
 i => 37, sum => 703
 i => 38, sum => 741
 i => 39, sum => 780
 i => 40, sum => 820
 i => 41, sum => 861
 i => 42, sum => 903
 i => 43, sum => 946
 i => 44, sum => 990
 i => 45, sum => 1035
 i => 46, sum => 1081
 i => 47, sum => 1128
 i => 48, sum => 1176
 i => 49, sum => 1225
 i => 50, sum => 1275
 i => 51, sum => 1326
 i => 52, sum => 1378
 i => 53, sum => 1431
 i => 54, sum => 1485
 i => 55, sum => 1540
 i => 56, sum => 1596
 i => 57, sum => 1653
 i => 58, sum => 1711
 i => 59, sum => 1770
 i => 60, sum => 1830
 i => 61, sum => 1891
 i => 62, sum => 1953
 i => 63, sum => 2016
 i => 64, sum => 2080
 i => 65, sum => 2145
 i => 66, sum => 2211
 i => 67, sum => 2278
 i => 68, sum => 2346
 i => 69, sum => 2415
 i => 70, sum => 2485
 i => 71, sum => 2556
 i => 72, sum => 2628
 i => 73, sum => 2701
 i => 74, sum => 2775
 i => 75, sum => 2850
 i => 76, sum => 2926
 i => 77, sum => 3003
 i => 78, sum => 3081
 i => 79, sum => 3160
 i => 80, sum => 3240
 i => 81, sum => 3321
 i => 82, sum => 3403
 i => 83, sum => 3486
 i => 84, sum => 3570
 i => 85, sum => 3655
 i => 86, sum => 3741
 i => 87, sum => 3828
 i => 88, sum => 3916
 i => 89, sum => 4005
 i => 90, sum => 4095
 i => 91, sum => 4186
 i => 92, sum => 4278
 i => 93, sum => 4371
 i => 94, sum => 4465
 i => 95, sum => 4560
 i => 96, sum => 4656
 i => 97, sum => 4753
 i => 98, sum => 4851
 i => 99, sum => 4950
 i => 100, sum => 5050
Traceback (most recent call last):
  File "C:/Users/82102/Desktop/파이썬/210508 python 노트.py", line 30, in <module>
    print(" sum = {}" .formata(sum))
AttributeError: 'str' object has no attribute 'formata'
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
 i =>  1, sum =>   1
 i =>  3, sum =>   4
 i =>  5, sum =>   9
 i =>  7, sum =>  16
 i =>  9, sum =>  25
 i => 11, sum =>  36
 i => 13, sum =>  49
 i => 15, sum =>  64
 i => 17, sum =>  81
 i => 19, sum => 100
 i => 21, sum => 121
 i => 23, sum => 144
 i => 25, sum => 169
 i => 27, sum => 196
 i => 29, sum => 225
 i => 31, sum => 256
 i => 33, sum => 289
 i => 35, sum => 324
 i => 37, sum => 361
 i => 39, sum => 400
 i => 41, sum => 441
 i => 43, sum => 484
 i => 45, sum => 529
 i => 47, sum => 576
 i => 49, sum => 625
 i => 51, sum => 676
 i => 53, sum => 729
 i => 55, sum => 784
 i => 57, sum => 841
 i => 59, sum => 900
 i => 61, sum => 961
 i => 63, sum => 1024
 i => 65, sum => 1089
 i => 67, sum => 1156
 i => 69, sum => 1225
 i => 71, sum => 1296
 i => 73, sum => 1369
 i => 75, sum => 1444
 i => 77, sum => 1521
 i => 79, sum => 1600
 i => 81, sum => 1681
 i => 83, sum => 1764
 i => 85, sum => 1849
 i => 87, sum => 1936
 i => 89, sum => 2025
 i => 91, sum => 2116
 i => 93, sum => 2209
 i => 95, sum => 2304
 i => 97, sum => 2401
 i => 99, sum => 2500
Traceback (most recent call last):
  File "C:/Users/82102/Desktop/파이썬/210508 python 노트.py", line 40, in <module>
    print(" sum = {}" .formata(sum))
AttributeError: 'str' object has no attribute 'formata'
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
Traceback (most recent call last):
  File "C:/Users/82102/Desktop/파이썬/210508 python 노트.py", line 43, in <module>
    print(" sum = {}" .formata(sum))
AttributeError: 'str' object has no attribute 'formata'
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
 i => 100, sum => 100
 i => 98, sum => 198
 i => 96, sum => 294
 i => 94, sum => 388
 i => 92, sum => 480
 i => 90, sum => 570
 i => 88, sum => 658
 i => 86, sum => 744
 i => 84, sum => 828
 i => 82, sum => 910
 i => 80, sum => 990
 i => 78, sum => 1068
 i => 76, sum => 1144
 i => 74, sum => 1218
 i => 72, sum => 1290
 i => 70, sum => 1360
 i => 68, sum => 1428
 i => 66, sum => 1494
 i => 64, sum => 1558
 i => 62, sum => 1620
 i => 60, sum => 1680
 i => 58, sum => 1738
 i => 56, sum => 1794
 i => 54, sum => 1848
 i => 52, sum => 1900
 i => 50, sum => 1950
 i => 48, sum => 1998
 i => 46, sum => 2044
 i => 44, sum => 2088
 i => 42, sum => 2130
 i => 40, sum => 2170
 i => 38, sum => 2208
 i => 36, sum => 2244
 i => 34, sum => 2278
 i => 32, sum => 2310
 i => 30, sum => 2340
 i => 28, sum => 2368
 i => 26, sum => 2394
 i => 24, sum => 2418
 i => 22, sum => 2440
 i => 20, sum => 2460
 i => 18, sum => 2478
 i => 16, sum => 2494
 i => 14, sum => 2508
 i => 12, sum => 2520
 i => 10, sum => 2530
 i =>  8, sum => 2538
 i =>  6, sum => 2544
 i =>  4, sum => 2548
 i =>  2, sum => 2550
Traceback (most recent call last):
  File "C:/Users/82102/Desktop/파이썬/210508 python 노트.py", line 43, in <module>
    print(" sum = {}" .formata(sum))
AttributeError: 'str' object has no attribute 'formata'
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
 이름은 : nuri
반갑습니다. nuri님
 이름은 : s
반갑습니다. s님
 이름은 : s
반갑습니다. s님
 이름은 : s
반갑습니다. s님
 이름은 : s
반갑습니다. s님
>>> s
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    s
sNameError: name 's' is not defined
>>> 
>>> 
Traceback (most recent call last):= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0

 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0

 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0

 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0

 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0
 i ==> 0Traceback (most recent call last):
  File "C:/Users/82102/Desktop/파이썬/210508 python 노트.py", line 57, in <module>
    print(" i ==> {}".format(i))
KeyboardInterrupt
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
 i ==> 0
 i ==> 1
 i ==> 2
 i ==> 3
 i ==> 4
 i ==> 5
 i ==> 6
 i ==> 7
 i ==> 8
 i ==> 9
 i ==> 10
>>> 
= RESTART: C:/Users/82102/Desktop/파이썬/210508 python 노트.py
i ==> 1
i ==> 2
i ==> 3
i ==> 4
i ==> 5
i ==> 6
i ==> 7
i ==> 8
i ==> 9
i ==> 10
sum = 55
>>> 
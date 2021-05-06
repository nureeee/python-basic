Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
>>> type(a)
<class 'list'>
>>> 
>>> len(a)
3
>>> a[0]
1
>>> a[1]
2
>>> a[2]
3
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> a[3] = 4
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[3] = 4
IndexError: list assignment index out of range
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
>>> a.append(66)
>>> a
[1, 2, 3, 4, 5, 66]
>>> a.append([88,99])
>>> a
[1, 2, 3, 4, 5, 66, [88, 99]]
>>> len(a)
7
>>> a[6]
[88, 99]
>>> a[6][]0
SyntaxError: invalid syntax
>>> a[6][0]
88
>>> a[6][1]
99
>>> a[1], a[2]
(2, 3)
>>> a[6][0] #리스트 안에 리스트
88
>>> a.append(100)
>>> a.pop()
100
>>> len(a)
7
>>> a.insert(2,7)
>>> a
[1, 2, 7, 3, 4, 5, 66, [88, 99]]
>>> a.insert(0,9)
>>> a
[9, 1, 2, 7, 3, 4, 5, 66, [88, 99]]
>>> a.reverse()
>>> a
[[88, 99], 66, 5, 4, 3, 7, 2, 1, 9]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'list'
>>> a.reverse()
>>> a
[9, 1, 2, 7, 3, 4, 5, 66, [88, 99]]
>>> a.pop()
[88, 99]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5, 7, 9, 66]
>>> a.sort(reverse=True)
>>> a
[66, 9, 7, 5, 4, 3, 2, 1]
>>> a.sort(reverse=False)
>>> a
[1, 2, 3, 4, 5, 7, 9, 66]
>>> a.remove(2)
>>> a
[1, 3, 4, 5, 7, 9, 66]
>>> a.remove(20)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.remove(20)
ValueError: list.remove(x): x not in list
>>> a.count(3)
1
>>> a
[1, 3, 4, 5, 7, 9, 66]
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.index(2)
ValueError: 2 is not in list
>>> a.index(3)
1
>>> a.clear()
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
>>> 
>>> 
>>> 
>>> a={1, 3, 5, 7, 9}
>>> del a
>>> a= [1, 3, 5, 7, 9]
>>> set = list(a)
>>> a
[1, 3, 5, 7, 9]
>>> set= set(a)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    set= set(a)
TypeError: 'list' object is not callable
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a= [1, 3, 5, 7, 9]
>>> ca = a.copy()
>>> a
[1, 3, 5, 7, 9]
>>> ca
[1, 3, 5, 7, 9]
>>> a.append(11)
>>> a
[1, 3, 5, 7, 9, 11]
>>> ca
[1, 3, 5, 7, 9]
>>> b=a
>>> a.append(13)
>>> a
[1, 3, 5, 7, 9, 11, 13]
>>> b
[1, 3, 5, 7, 9, 11, 13]
>>> ca
[1, 3, 5, 7, 9]
>>> a.append(15)
>>> 
>>> a
[1, 3, 5, 7, 9, 11, 13, 15]
>>> b
[1, 3, 5, 7, 9, 11, 13, 15]
>>> ca
[1, 3, 5, 7, 9]
>>> id(a)
2066536459584
>>> id(b)
2066536459584
>>> id(ca)
2066536641344
>>> a is b
True
>>> a is ca
False
>>> 
>>> 
>>> del a
>>> delb
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    delb
NameError: name 'delb' is not defined
>>> del b
>>> del ca
>>> a = [1, 3, 5, 7, 9, 11, 13, 15]
>>> b= [1, 3, 5, 7, 9, 11, 13, 15]
>>> a[3]
7
>>> a[5]
11
>>> a[:3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[:3]
[1, 3, 5]
>>> a[5:]
[11, 13, 15]
>>> a[2:6]
[5, 7, 9, 11]
>>> a[:5:3]
[1, 7]
>>> a[-1]
15
>>> a[-6:3]
[5]
>>> a[-6:-3]
[5, 7, 9]
>>> a[-6:4]
[5, 7]
>>> a[-6:1]
[]
>>> a[1:-6]
[3]
>>> b=[21,,23,25]
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> del a
>>> delb
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    delb
NameError: name 'delb' is not defined
>>> del b
>>> a=[1, 2, 3, 4, 5]
>>> a*2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> a+2
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    a+2
TypeError: can only concatenate list (not "int") to list
>>> a - 2
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    a - 2
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> a/2
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a/2
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> b= [10, 20, 30 ]
>>> b.append('seoul')
>>> b
[10, 20, 30, 'seoul']
>>> b.append('busan')
>>> b
[10, 20, 30, 'seoul', 'busan']
>>> b.append(4.789)
>>> len(d)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    len(d)
NameError: name 'd' is not defined
>>> len(b)
6
>>> ta = (1, 2, 3, 4, 5)
>>> type(ta)
<class 'tuple'>
>>> ta.count(2)
1
>>> ta.index(5)
4
>>> a[0]
1
>>> a[o] = 100
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    a[o] = 100
NameError: name 'o' is not defined
>>> a[0] = 100
>>> ta[0]
1
>>> ta[1]
2
>>> ta[2] = 100
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    ta[2] = 100
TypeError: 'tuple' object does not support item assignment
>>> #tuple은 값 변경 불가
>>> k= 1,2,3
>>> k
(1, 2, 3)
>>> type(k)
<class 'tuple'>
>>> k1= (1, 2, 3)
>>> k1[2]
3
>>> type(k1)
<class 'tuple'>
>>> k= list(k)
>>> k
[1, 2, 3]
>>> type(k)
<class 'list'>
>>> k.append(5)
>>> k.append(7)
>>> k= tuple(k)
>>> k2=10, 20 30  #패킹
SyntaxError: invalid syntax
>>> k2=10, 20, 30
>>> k10, k20, k30 = k2
>>> k10
10
>>> k20
20
>>> k30  #언패킹
30
>>> k10,k30 =k30, k10 #값 맞교환(정수, 문자열 다 가능)
>>> s1 = "서울"
>>> b1 = "부산"
>>> s1, b1 = b1, s1
>>> print(s1, b1)
부산 서울
>>> a = [1, 2, 3]
>>> kk =[55,66]
>>> ca= a.copy()
>>> import copy
>>> cca = copy.copy(a)
>>> cca
[1, 2, 3]
>>> ca
[1, 2, 3]
>>> c
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> a
[1, 2, 3]
>>> kk
[55, 66]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a= [1, 2, 3, 4, 5, 6]
>>> a[-2:-4]
[]
>>> a[-4:-2]
[3, 4]
>>> 
>>> 
>>> 
>>> 
>>> a={1, 2, 3, 4, 5}
>>> b={2, 4, 6, 8, 10}
>>> type(a), type(b)
(<class 'set'>, <class 'set'>)
>>> a|b
{1, 2, 3, 4, 5, 6, 8, 10}
>>> a|b #합집합
{1, 2, 3, 4, 5, 6, 8, 10}
>>> a & b  #교집합
{2, 4}
>>> a-b
{1, 3, 5}
>>> b-a
{8, 10, 6}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 8, 10}
>>> a
{1, 2, 3, 4, 5}
>>> a.intersection(b)
{2, 4}
>>> a.di(b)
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    a.di(b)
AttributeError: 'set' object has no attribute 'di'
>>> a.difference(b)
{1, 3, 5}
>>> len(a)
5
>>> len(b)
5
>>> a[0] #set은 순차개념이 없다.
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    a[0] #set은 순차개념이 없다.
TypeError: 'set' object is not subscriptable
>>> a.add(6)
>>> a.add(7)
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> a.remove(4)
>>> a.discard(2)
>>> a.add(3)
>>> a
{1, 3, 5, 6, 7}
>>> a.add(5)
>>> a
{1, 3, 5, 6, 7}
>>> c= {5, 6}
>>> c.issubset(a)
True
>>> c.issubset(b)
False
>>> a.issubset (b)
False
>>> a.issuperset(b)
False
>>> a.issuperset(c)
True
>>> c.issuperset(a)
False
>>> s1 = {'seoul', 'busan', 'incheon'}
>>> s1
{'incheon', 'busan', 'seoul'}
>>> s2 ={'seoul', 'la'}
>>> s2 ={'seoul'}
>>> s1- s3
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    s1- s3
NameError: name 's3' is not defined
>>> s1|s2
{'incheon', 'busan', 'seoul'}
>>> s1&s3
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    s1&s3
NameError: name 's3' is not defined
>>> s1 & s3
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    s1 & s3
NameError: name 's3' is not defined
>>> s1&s3
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    s1&s3
NameError: name 's3' is not defined
>>> s1 - s3
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    s1 - s3
NameError: name 's3' is not defined
>>> s`-s3
SyntaxError: invalid syntax
>>> s3 & s1
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    s3 & s1
NameError: name 's3' is not defined
>>> s3= {'sseoul'}
>>> s3= {'seoul'}
>>> s1-s3
{'incheon', 'busan'}
>>> s1|s2
{'incheon', 'busan', 'seoul'}
>>> s1&s3
{'seoul'}
>>> s3.issu(s1)
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    s3.issu(s1)
AttributeError: 'set' object has no attribute 'issu'
>>> s3.issubset(s1)
True
>>> s3.issuperset(s1)
False
>>> s5 = {20, 40, 50, 4.789, '서울', '부산'}
>>> s5
{'서울', 50, 4.789, '부산', 20, 40}
>>> print(s5)
{'서울', 50, 4.789, '부산', 20, 40}
>>> type(s5)
<class 'set'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> dictset()
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    dictset()
NameError: name 'dictset' is not defined
>>> dic(set)
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    dic(set)
NameError: name 'dic' is not defined
>>> a
{1, 3, 5, 6, 7}
>>> del a
>>> a={'이름' : '김철수', '나이' : 30, '직업' : '학생'}
>>> a['이름']
'김철수'
>>> a['나이']
30
>>> a['직업']
'학생'
>>> a.items()
dict_items([('이름', '김철수'), ('나이', 30), ('직업', '학생')])
>>> a.key()
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    a.key()
AttributeError: 'dict' object has no attribute 'key'
>>> a.keys()
dict_keys(['이름', '나이', '직업'])
>>> a.values()
dict_values(['김철수', 30, '학생'])
>>> b= {1:'one', 2: 'two', 3: 'three'}
>>> type(b)
<class 'dict'>
>>> b[1]
'one'

>>> for i,j in b.items():
	print(i,j)

	
1 one
2 two
3 three
>>> for key,while in b.items():
	print(key,"---->", value)
	
SyntaxError: invalid syntax
>>> for key,valuein b.items():
	print(key,"---->", value)
	
SyntaxError: invalid syntax
>>> for key,valuein a.items():
	print(key,"---->", value)
	
SyntaxError: invalid syntax
>>> for key,valuein a.items():
	print(key,"---->", value)
	
SyntaxError: invalid syntax
>>> for key,value in a.items():
	print(key,"---->", value)

	
이름 ----> 김철수
나이 ----> 30
직업 ----> 학생
>>> print(a,b)
{'이름': '김철수', '나이': 30, '직업': '학생'} {1: 'one', 2: 'two', 3: 'three'}
>>> b.pop(1)
'one'
>>> b.get(3)
'three'
>>> b.update({4:'four'})
>>> b
{2: 'two', 3: 'three', 4: 'four'}
>>> b.update({5:'five'})
>>> b.get(4)
'four'
>>> b
{2: 'two', 3: 'three', 4: 'four', 5: 'five'}
>>> b.pop(4)
'four'
>>> b
{2: 'two', 3: 'three', 5: 'five'}
>>> b.popitem()
(5, 'five')
>>> b
{2: 'two', 3: 'three'}
>>> 
>>> b.clear()
>>> b
{}
>>> week = {0:'일요일', 1:'월요일', 2:'화요일', 3:'수요일'}
>>> for key, value in week.items():
	print(key,'==>', value)

	
0 ==> 일요일
1 ==> 월요일
2 ==> 화요일
3 ==> 수요일
>>> w1 = {4:'목요일', 5:'금요일', 6:'토요일'}
>>> week.update(w1)
>>> week
{0: '일요일', 1: '월요일', 2: '화요일', 3: '수요일', 4: '목요일', 5: '금요일', 6: '토요일'}
>>> for i,j in week.items():
	print(i,j)

	
0 일요일
1 월요일
2 화요일
3 수요일
4 목요일
5 금요일
6 토요일
>>> 
>>> 
>>> a = [1, 2, 3, 4, 5]
>>> b= (3, 5, 7, 9)
>>> c = {3, 5, 7, 9}
>>> c2 = {1, 2, 3, 5}
>>> 2 in a
True
>>> 9 in b
True
>>> 3 in c
True
>>> 20 in c
False
>>> la =a
>>> la==a
True
>>> a is la
True
>>> id(a)
2066536544448
>>> id(la)
2066536544448
>>> ca= a.copy()
>>> a==ca
True
>>> a is ca
False
>>> c|c2
{1, 2, 3, 5, 7, 9}
>>> c & c2
{3, 5}
>>> c - c2
{9, 7}
>>> c.symmetric_difference(c2)
{1, 2, 7, 9}
>>> type(a)
<class 'list'>
>>> ta= tuple(a)
>>> ta
(1, 2, 3, 4, 5)
>>> la = list(ta)
>>> 
>>> #포함하고 있는가 in
>>> #값이 같은가?==
>>> #id가 같은가? is
>>> 
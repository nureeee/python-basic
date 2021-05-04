Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> k="korea"
>>> type(k)
<class 'str'>
>>> k[0]
'k'
>>> k[1]
'o'
>>> k[5]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    k[5]
IndexError: string index out of range
>>> k[-1]
'a'
>>> k[-2]
'e'
>>> k[-5]
'k'
>>> k
'korea'
>>> k.find('k')
0
>>> k.find('o')
1
>>> k.find('T')
-1
>>> k.rfind('T')
-1
>>> k.rfind('k')
0
>>> k2=k*3
>>> k2
'koreakoreakorea'
>>> k2.find('a)
	
SyntaxError: EOL while scanning string literal
>>> k2.rfind('a')
14
>>> k2.count('a')
3
>>> k2.count('o')
3
>>> k2.count('R')
0
>>> k2.count('e')
3
>>> k2.startswid('R')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    k2.startswid('R')
AttributeError: 'str' object has no attribute 'startswid'
>>> k2.startswidch('R')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    k2.startswidch('R')
AttributeError: 'str' object has no attribute 'startswidch'
>>> k2.startswiss('R')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    k2.startswiss('R')
AttributeError: 'str' object has no attribute 'startswiss'
>>> k2.startswith('R')
False
>>> k2.startswith('k')
True
>>> k2.startswith('p')
False
>>> k2.startswith('e')
False
>>> k2.endswith('a')
True
>>> k2.endswith('b')
False
>>> k2
'koreakoreakorea'
>>> k2.upper()
'KOREAKOREAKOREA'
>>> k2
'koreakoreakorea'
>>> k3=k2.upper()
>>> k3
'KOREAKOREAKOREA'
>>> k3.lower()
'koreakoreakorea'
>>> s='  seoul  '
>>> s
'  seoul  '
>>> k
'korea'
>>> k2
'koreakoreakorea'
>>> len(k)
5
>>> len(2k)
SyntaxError: invalid syntax
>>> len(k2)
15
>>> len(s)
9
>>> s.strip()
'seoul'
>>> s.lstrip()
'seoul  '
>>> s.rstrip()
'  seoul'
>>> s='  seoul  '
>>> s='  seo  ul  '
>>> s.strip()
'seo  ul'
>>> 'T'.isalpha()
True
>>> '0'.isalpha()
False
>>> '5'.isalpha()
False
>>> '$'.isalpha()
False
>>> '7'.isalpha()
False
>>> '7'.isnumeric()
True
>>> '$'.isnumeric()
False
>>> 'A'.isnumeric()
False
>>> 
>>> print(s, "기 좋아요")
  seo  ul   기 좋아요
>>> s=seoul
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s=seoul
NameError: name 'seoul' is not defined
>>> s=(seoul)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s=(seoul)
NameError: name 'seoul' is not defined
>>> s='seoul'
>>> print(s, "가 좋아요")
seoul 가 좋아요
>>> print(s,"가 좋아요")
seoul 가 좋아요
>>> print('s',"가 좋아요")
s 가 좋아요
>>> s.replace('e', 'E')
'sEoul'
>>> s
'seoul'
>>> b1= "서울이 좋아요"
>>> b2=b1.replace("서울", "부산")
>>> ㅠ2
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    ㅠ2
NameError: name 'ᅲ2' is not defined
>>> b2
'부산이 좋아요'
>>> b1, b2
('서울이 좋아요', '부산이 좋아요')
>>> bc ="kbs mbc sbs ebs ytn"
>>> bc
'kbs mbc sbs ebs ytn'
>>> bc2 = bc.upper()
>>> bc2
'KBS MBC SBS EBS YTN'
>>> type(bc)
<class 'str'>
>>> type(bc2)
<class 'str'>
>>> bc3= bc2.split()
>>> bc3
['KBS', 'MBC', 'SBS', 'EBS', 'YTN']
>>> type(bc3), len(bc3)
(<class 'list'>, 5)
>>> bc4 ="kbs/mbc/sbs"
>>> bc4
'kbs/mbc/sbs'
>>> bc5=bc4.split('/')
>>> bc5
['kbs', 'mbc', 'sbs']
>>> bc4="kbs:mbc:sbs"
>>> bc4
'kbs:mbc:sbs'
>>> bc5=bc4.split(':')
>>> bc5
['kbs', 'mbc', 'sbs']
>>> a=apple
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a=apple
NameError: name 'apple' is not defined
>>> a+4 #에러발생
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a+4 #에러발생
NameError: name 'a' is not defined
>>> a*3
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a*3
NameError: name 'a' is not defined
>>> b = "banana"
>>> b
'banana'
>>> a+b
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a+b
NameError: name 'a' is not defined
>>> b*4
'bananabananabananabanana'
>>> a='apple'
>>> b='pine'
>>> print(a, b, a+b)
apple pine applepine
>>> b+a
'pineapple'
>>> a*3+b*2
'appleappleapplepinepine'
>>>  a = ("apple", "banana","kiwi")
 
SyntaxError: unexpected indent
>>> a = ("apple", "banana","kiwi")
>>> a
('apple', 'banana', 'kiwi')
>>> a1 = a.split()
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a1 = a.split()
AttributeError: 'tuple' object has no attribute 'split'
>>> a=" 서울 남산 부산 경주"
>>> 
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
' 서울 남산 부산 경주'
>>> b = a.split()
>>> b
['서울', '남산', '부산', '경주']
>>> type(b)
<class 'list'>
>>> c = (인천 공항 남산)
SyntaxError: invalid syntax
>>> c = ('인천', '공항', '남산')
>>> ㅊ
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    ㅊ
NameError: name 'ᄎ' is not defined
>>> c
('인천', '공항', '남산')
>>> d = c.split()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    d = c.split()
AttributeError: 'tuple' object has no attribute 'split'
>>> c = ['인천', '공항', '남산']
>>> c
['인천', '공항', '남산']
>>> d = c.sort
>>> 
>>> d
<built-in method sort of list object at 0x0000020F00205600>
>>> 
>>> 
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'b1', 'b2', 'bc', 'bc2', 'bc3', 'bc4', 'bc5', 'c', 'd', 'k', 'k2', 'k3', 's']
>>> SUM
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    SUM
NameError: name 'SUM' is not defined
>>> Sum
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    Sum
NameError: name 'Sum' is not defined
>>> a
' 서울 남산 부산 경주'
>>> aa
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    aa
NameError: name 'aa' is not defined
>>> del Sum, i, j, k, k2, k3, s, bc5, bc4, bc3, bc2, bc1, aa, a
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    del Sum, i, j, k, k2, k3, s, bc5, bc4, bc3, bc2, bc1, aa, a
NameError: name 'Sum' is not defined
>>> chr(65)
'A'
>>> ord('A')
65
>>> chr(65)
'A'
>>> chr(a)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    chr(a)
TypeError: an integer is required (got type str)
>>> chr(66)
'B'
>>> chr(67)
'C'
>>> chr(98)
'b'
>>>          
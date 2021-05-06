Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= [4, 6, 5.6, 7.5, 'ace', 'korea', 3]
>>> a
[4, 6, 5.6, 7.5, 'ace', 'korea', 3]
>>> type(a)
<class 'list'>
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> b= ['서울', '부산', '서울']
>>> b.sort()
>>> b
['부산', '서울', '서울']
>>> a.pop()
3
>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'b
SyntaxError: invalid syntax
>>> a
[4, 5.6, 6, 7.5, 'ace', 'korea']
>>> b
['부산', '서울', '서울']
>>> a.__eq__(b)
False
>>> a==b
False
>>> a.append(b)
>>> b.append(b)
>>> a
[4, 5.6, 6, 7.5, 'ace', 'korea', ['부산', '서울', '서울', [...]]]
>>> b
['부산', '서울', '서울', [...]]
>>> t = (30, 50, 70)
>>> lenn(t)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    lenn(t)
NameError: name 'lenn' is not defined
>>> len(t)
3

>>> t[0]
30
>>> t[1]
50
>>> t[0]+ t[1]
80

>>> t.index()30
SyntaxError: invalid syntax
>>> t.index(30)
0
>>> t.count(30)
1
>>> t.count()220
SyntaxError: invalid syntax
>>> t.count(220)
0
>>> t
(30, 50, 70)
>>> t = (4, 5, 6)
>>> t
(4, 5, 6)
>>> type(t)
<class 'tuple'>
>>> list(t)
[4, 5, 6]
>>> type
<class 'type'>
>>> type(t)
<class 'tuple'>
>>> tt = list(t)
>>> tt
[4, 5, 6]
>>> tt[0] =2
>>> tt
[2, 5, 6]
>>> t=tuple(tt)
>>> t
(2, 5, 6)
>>> a==b
False
>>> i= 100
>>> j=200
>>> i
100
>>> j
200
>>> t=i
>>> i=j
>>> j=t
>>> i
200
>>> j
100
>>> t
100
>>> i, j =j, i
>>> i
100
>>> j
200
>>> i, j = j, t
>>> i
200
>>> t
100
>>> j
100
>>> z = 10, 20, 30
>>> z
(10, 20, 30)
>>> type()z
SyntaxError: invalid syntax
>>> type(z)
<class 'tuple'>
>>> z1, z2, z3 = z
>>> z1
10
>>> z2
20
>>> z3
30
>>> z = 10, 20, 30
>>> z2, z3=z
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    z2, z3=z
ValueError: too many values to unpack (expected 2)

>>> z = 10, 20, 30
>>> z
(10, 20, 30)
>>> type()z
SyntaxError: invalid syntax
>>> type(z)
<class 'tuple'>
>>> z1, z2, z3 = z
>>> z1
10
>>> z2
20
>>> z3
30
SyntaxError: multiple statements found while compiling a single statement
>>> z = 10, 20, 30
>>> z
(10, 20, 30)
>>> z1, z2, z3 =z
>>> z1
10
>>> z2
20
>>> z3
30
>>> #위의 내용 확인
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'i', 'j', 't', 'tt', 'z', 'z1', 'z2', 'z3']
>>> del a, b, i,, j, t, tt, z, z1,z2,z3
SyntaxError: invalid syntax
>>> del a, b, i, j, t, tt, z, z1,z2,z3
>>> 
>>> 
>>> 
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
>>> 
>>> 
>>> 
>>> a= {1, 2, 3, 4, 5}
>>> b= {2, 4, 6}
>>> type(a)
<class 'set'>
>>> type(b)
<class 'set'>
>>> a
{1, 2, 3, 4, 5}
>>> b
{2, 4, 6}
>>> a| b
{1, 2, 3, 4, 5, 6}
>>> a&b
{2, 4}
>>> a-b
{1, 3, 5}
>>> b-a
{6}
>>> a.union(b)
{1, 2, 3, 4, 5, 6}
>>> a | b
{1, 2, 3, 4, 5, 6}
>>> a.intersection(b)
{2, 4}
>>> a&b
{2, 4}

>>> len(a)
5
>>> len(b)
3
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
>>> a[1]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a[1]
TypeError: 'set' object is not subscriptable
>>> #집합은 순서에 대한 개념이 없다.
>>> a.add(5)
>>> a
{1, 2, 3, 4, 5}
>>> a.add(2)
>>> #집합은 리스트와 다르게 중복의 개념이 없다.
>>> a.remove(1)
>>> a
{2, 3, 4, 5}
>>> 2 in a
True
>>> (2),issubclass(a)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    (2),issubclass(a)
TypeError: issubclass expected 2 arguments, got 1
>>> a ={2, 3}
>>> a
{2, 3}
>>> a.add(1, 3)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a.add(1, 3)
TypeError: set.add() takes exactly one argument (2 given)
>>> a.add(1)
>>> a
{1, 2, 3}
>>> a2={2, 3}
>>> a2.issubset(a)
True
>>> a2.issuperset(a)
False
>>> d={'이름':'강호동', '나이':51, '직업': 'MC'}
>>> type(d)
<class 'dict'>
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['이름']
'강호동'
>>> d['나이']
51
>>> d.keys()
dict_keys(['이름', '나이', '직업'])
>>> d.values()
dict_values(['강호동', 51, 'MC'])
>>> d.items()
dict_items([('이름', '강호동'), ('나이', 51), ('직업', 'MC')])
>>> for key, value, in d.items():
	pprint(key, value)

	
Traceback (most recent call last):
  File "<pyshell#138>", line 2, in <module>
    pprint(key, value)
NameError: name 'pprint' is not defined
>>> for key, value, in d.items():
	print(key, value)

	
이름 강호동
나이 51
직업 MC
>>> for i, j in d.items():
	print(i= ===>, j)
	
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> for i, j in d.items():
	print(i= '===>', j)
	
SyntaxError: positional argument follows keyword argument
>>> for i, j in d.items():
	print(i, '===>', j)

	
이름 ===> 강호동
나이 ===> 51
직업 ===> MC
>>> dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> dir(d)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d
{'이름': '강호동', '나이': 51, '직업': 'MC'}
>>> d.update({'수입: 30'})
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    d.update({'수입: 30'})
ValueError: dictionary update sequence element #0 has length 6; 2 is required
>>> ㅇ
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    ㅇ
NameError: name 'ᄋ' is not defined
>>> d.update({'수입': 30})
>>> d
{'이름': '강호동', '나이': 51, '직업': 'MC', '수입': 30}
>>> d.get('수입')
30
>>> d.get('나이')
51
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d.popitem()
('수입', 30)
>>> dd
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    dd
NameError: name 'dd' is not defined

>>> d
{'이름': '강호동', '나이': 51, '직업': 'MC'}
>>> #PDF 20p 내용
>>> a
{1, 2, 3}
>>> 2 in a
True
>>> 2 in not a
SyntaxError: invalid syntax
>>> 2 not in a
False
>>> aaa = a
>>> id(a)
2490530386656
>>> id(aaa)
2490530386656
>>> a is aaa
True

>>> aaa is a
True
>>> ac = a.copy()
>>> id(ac)
2490530388896
>>> id(a)
2490530386656
>>> a is ac
False
>>> a==ac
True
>>> True & False
False
>>> True | False
True
>>> True ^ True
False
>>> True ^ False
True
>>> ~ True
-2
>>> 
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [2, 4, 6, 8]
>>> len(a)
4
>>> for i, j in enumerate(a):
	print(i, j)

0 2
1 4
2 6
3 8
>>> for i in a:
	print(a)

	
[2, 4, 6, 8]
[2, 4, 6, 8]
[2, 4, 6, 8]
[2, 4, 6, 8]
>>> for i in a:
	print(i)

	
2
4
6
8
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'i', 'j']
>>> del a[3]
>>> a
[2, 4, 6]
>>> a.remove(4)
>>> a
[2, 6]
>>> a.pop()
6
>>> a.append(3)
>>> a.append(5)
>>> a
[2, 3, 5]
>>> b = {'이름' : '철수',  '나이':20, '직업':'학생'}
>>> type(b)
<class 'dict'>
>>> b.items()
dict_items([('이름', '철수'), ('나이', 20), ('직업', '학생')])
>>> b.keys()
dict_keys(['이름', '나이', '직업'])
>>> b.values()
dict_values(['철수', 20, '학생'])
>>> for key, value in b.items():
	print(key, value)

	
이름 철수
나이 20
직업 학생
>>> dir(b)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> b['이름']
'철수'
>>> b['학생']
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    b['학생']
KeyError: '학생'
>>> b.popitem()
('직업', '학생')
>>> b
{'이름': '철수', '나이': 20}
>>> b.update({'고햘':'부산'})
>>> ㅠ
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    ㅠ
NameError: name 'ᅲ' is not defined
>>> b.update({'고햘':'부산'})
>>> b
{'이름': '철수', '나이': 20, '고햘': '부산'}
>>> a
[2, 3, 5]
>>> a = [1, 2, 3, 4]
>>> sum(a)
10
>>> sum(1, 2, 3)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    sum(1, 2, 3)
TypeError: sum() takes at most 2 arguments (3 given)
>>> sum([1, 2, 3])
6
>>> def mysum(*x):
	Sum = 0
	for i in x:
		Sum = Sum + i

		
>>> def mysum(*x):
	Sum = 0
	for i in x:
		Sum = Sum + i
	return Sum

>>> mtsum(2, 3, 4)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    mtsum(2, 3, 4)
NameError: name 'mtsum' is not defined
>>> mysum(2, 3, 4)
9
>>> mysum(2, 3, 4, 5, 6, 7, 8)
35
>>> mysum(2)
2
>>> mysum(a)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    mysum(a)
  File "<pyshell#50>", line 4, in mysum
    Sum = Sum + i
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> mysum(*a)
10
>>> #위의 내용은 *이 들어가 a의 리스트를 하나로 보는 것이 아니라 *a는 개별의 값으로 계산한다.
>>> def Add(x=30, y=50):
	return x+y
Add(100, 200)
SyntaxError: invalid syntax
>>> def Add(x=30, y=50):
	return x+y

>>> Add(100, 200)
300
>>> Add(3)
53
>>> Add()
80
>>> Add(y=100, x=200)
300
>>> a = [2, 3, [4, 5]]
>>> mySum(*a)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    mySum(*a)
NameError: name 'mySum' is not defined
>>> a.pop()
[4, 5]
>>> mySum(*a)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    mySum(*a)
NameError: name 'mySum' is not defined
>>> mysum(*a)
5
>>> a.append([2, 3])
>>> a
[2, 3, [2, 3]]
>>> mysum(*a)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    mysum(*a)
  File "<pyshell#50>", line 4, in mysum
    Sum = Sum + i
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> def Add5(x, y):
	return None

>>> k = 1, 2, 3
>>> 
>>> k
(1, 2, 3)
>>> k[0]
1
>>> k[1] = 44
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    k[1] = 44
TypeError: 'tuple' object does not support item assignment
>>> k = 1, 2, 3   #packing
>>> k1, k2, k3 = k  #unpacking
>>> k1
1
>>> def f1(x):
	x*x

	
>>> f1(1)
>>> a = [1, 2, 3, 4]
>>> pow(2, 3)
8
>>> pow(2, 10)
1024
>>> for i in a:
	print(i, i*i)

	
1 1
2 4
3 9
4 16
>>> def f1(x):
	return x*x
for i in a:
	f1(i)
	
SyntaxError: invalid syntax
>>> def f1(x):
	return x*x

>>> 
>>> for i in a:
	f1(i)

	
1
4
9
16
>>> list(map(f1, a))
[1, 4, 9, 16]
>>> list(filter(f1, a))
[1, 2, 3, 4]
>>> list(filter(lambda x : x+x, a))
[1, 2, 3, 4]
>>> aa = 1200
>>> aa == 1000
False
>>> aa + 30
1230
>>> aa
1200
>>> aa = aa+30
>>> aa
1230
>>>  aa += 30
 
SyntaxError: unexpected indent
>>> aa += 30
>>> aa.__add__(30)
1290
>>> aa.__eq__(1000)
False
>>> dir(aa)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> S = 0
>>> 
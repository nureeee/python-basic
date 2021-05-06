Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a =[3, 6, 9]
>>> type(a)
<class 'list'>
>>> a[0]
3
>>> a[1]
6
>>> a[2]
9
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> len(a)
3
>>> b= [6, 8, 9]
>>> a
[3, 6, 9]
>>> b
[6, 8, 9]

>>> a+b
[3, 6, 9, 6, 8, 9]
>>> ab = a+b
>>> a
[3, 6, 9]
>>> b
[6, 8, 9]
>>> ab
[3, 6, 9, 6, 8, 9]
>>> a.extend(b)
>>> a
[3, 6, 9, 6, 8, 9]
>>> len(a)
6
>>> a[5]
9
>>> a[5]=99
>>> a
[3, 6, 9, 6, 8, 99]
>>> a[6]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[6]
IndexError: list index out of range
>>> a[6] =77
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a[6] =77
IndexError: list assignment index out of range
>>> a.append(77)
>>> a.(44)
SyntaxError: invalid syntax
>>> a.append(44)

>>> a
[3, 6, 9, 6, 8, 99, 77, 44]
>>> len(8)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    len(8)
TypeError: object of type 'int' has no len()
>>> len(a)
8
>>> a.append(3,4)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.append(3,4)
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append([66, 33])
>>> a
[3, 6, 9, 6, 8, 99, 77, 44, [66, 33]]
>>> a.extend([22,88])
>>> a
[3, 6, 9, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.insert(2, 80)
>>> a
[3, 6, 80, 9, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.insert(4,45)
>>> a
[3, 6, 80, 9, 45, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.insert(0,555)
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.insert(0, 555,\)
	 
SyntaxError: unexpected character after line continuation character
>>> a.insert(0, 555,/)
SyntaxError: invalid syntax
>>> a.insert(0, 555,2)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.insert(0, 555,2)
TypeError: insert expected 2 arguments, got 3
>>> a.pop()
88
>>> a.pop()
22
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, 44, [66, 33]]
>>> a.pop()
[66, 33]
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, 44]
>>> a.index(3)
1
>>> a.index(55)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.index(55)
ValueError: 55 is not in list
>>> a.index(555)
0
>>> a.index(44)
10
>>> a.index(443)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.index(443)
ValueError: 443 is not in list

>>> a.pop() =f
SyntaxError: cannot assign to function call
>>> a.append()b
SyntaxError: invalid syntax
>>> a.append(b)
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, 44, [6, 8, 9]]
>>> a.remove(44)
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, [6, 8, 9]]
>>> a.remove([6])
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.remove([6])
ValueError: list.remove(x): x not in list
>>> a.pop()
[6, 8, 9]
>>> a.pop()=t
SyntaxError: cannot assign to function call
>>> t = a.pop()
>>> t
77
>>> a.append(b)
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, [6, 8, 9]]
>>> tt =a.pop()
>>> tt
[6, 8, 9]
>>> tt[2] = 66667
>>> tt
[6, 8, 66667]
>>> a.append(tt)
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, [6, 8, 66667]]
>>> a.count(9)
1
>>> a.count()6
SyntaxError: invalid syntax
>>> a.count(6)
2
>>> a.del(6)
SyntaxError: invalid syntax
>>> del(a[4])
>>> a
[555, 3, 6, 80, 45, 6, 8, 99, [6, 8, 66667]]
>>> a.remmove(6)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.remmove(6)
AttributeError: 'list' object has no attribute 'remmove'
>>> a.remove(6)
>>> a
[555, 3, 80, 45, 6, 8, 99, [6, 8, 66667]]
>>> a.remove([0])
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.remove([0])
ValueError: list.remove(x): x not in list
>>> a
[555, 3, 80, 45, 6, 8, 99, [6, 8, 66667]]
>>> aa = a
>>> id(a)
1965200146240
>>> id(aa)
1965200146240
>>> a[1]33333
SyntaxError: invalid syntax
>>> a[1]=33333
>>> aa
[555, 33333, 80, 45, 6, 8, 99, [6, 8, 66667]]
>>> a
[555, 33333, 80, 45, 6, 8, 99, [6, 8, 66667]]
>>> aaa=a.copy()
>>> a
[555, 33333, 80, 45, 6, 8, 99, [6, 8, 66667]]
>>> a[1] =44
>>> a
[555, 44, 80, 45, 6, 8, 99, [6, 8, 66667]]
>>> aaa
[555, 33333, 80, 45, 6, 8, 99, [6, 8, 66667]]
>>> a.reverse()
>>> a
[[6, 8, 66667], 99, 8, 6, 45, 80, 44, 555]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'list'
>>> a.del(0)
SyntaxError: invalid syntax
>>> a.remove([6, 8, 66667])
>>> a
[99, 8, 6, 45, 80, 44, 555]
>>> a.reverse()
>>> a
[555, 44, 80, 45, 6, 8, 99]
>>> a.sort(reverse=True)
>>> a
[555, 99, 80, 45, 44, 8, 6]
>>> a.remove(22)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.remove(22)
ValueError: list.remove(x): x not in list
>>> len(a)
7
>>> a.clear(a)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a.clear(a)
TypeError: list.clear() takes no arguments (1 given)
>>> a.clear()
>>> a
[]
>>> a= 4, 5, 6
>>> a
(4, 5, 6)
>>> a=  [5, 6, 7]
>>> a
[5, 6, 7]
>>> a.del(a[2])
SyntaxError: invalid syntax
>>> del(a[2])
>>> a
[5, 6]
>>> a.index(0)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.index(0)
ValueError: 0 is not in list
>>> a.index(6)
1
>>> a=[3, 6, 5, 0, 2]
>>> a
[3, 6, 5, 0, 2]
>>> a.pop()
2
>>> a.extend([3, 5, 6])
>>> a
[3, 6, 5, 0, 3, 5, 6]
>>> a.extend(3, 5, 6)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    a.extend(3, 5, 6)
TypeError: list.extend() takes exactly one argument (3 given)
>>> a.append(b)
>>> a
[3, 6, 5, 0, 3, 5, 6, [6, 8, 66667]]
>>> a.pop()=yy
SyntaxError: cannot assign to function call
>>> a.pop()
[6, 8, 66667]
>>> a.pop() = yy
SyntaxError: cannot assign to function call
>>> a.pop() =yy
SyntaxError: cannot assign to function call
>>> yy= a.pop()
>>> yy
6
>>> a.append(b)
>>> a.pop()
[6, 8, 66667]
>>> yy= a.pop()
>>> yy.remove(6)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    yy.remove(6)
AttributeError: 'int' object has no attribute 'remove'
>>> del(yy[0])
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    del(yy[0])
TypeError: 'int' object does not support item deletion
>>> yy[2] = 222
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    yy[2] = 222
TypeError: 'int' object does not support item assignment
>>> yy[0]= 1
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    yy[0]= 1
TypeError: 'int' object does not support item assignment
>>> 
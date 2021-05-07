Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: C:/dd/210507.py ======================
만수르 님은 돈이 많아요..
전용진 님은 돈이 많아요..
>>> 
====================== RESTART: C:/dd/210507.py ======================
만수르 님은 돈이 많아요..
전용진 님은 돈이 많아요..
3
6
9
[3, 6, 9]
>>> 
====================== RESTART: C:/dd/210507.py ======================
만수르 님은 돈이 많아요..
전용진 님은 돈이 많아요..
3
6
9
[3, 6, 9]
(3, 6, 9)
>>> 
====================== RESTART: C:/dd/210507.py ======================
만수르 님은 돈이 많아요..
전용진 님은 돈이 많아요..
Traceback (most recent call last):
  File "C:/dd/210507.py", line 22, in <module>
    a = b
NameError: name 'b' is not defined
>>> 
====================== RESTART: C:/dd/210507.py ======================
만수르 님은 돈이 많아요..
전용진 님은 돈이 많아요..
3
6
9
[3, 6, 9] 2484988166080
2484988166080 2484988166080
3  6  9  
>>> 
====================== RESTART: C:/dd/210507.py ======================
만수르 님은 돈이 많아요..
전용진 님은 돈이 많아요..
3
6
9
[3, 6, 9] 1503651839936
1503651839936 1503651839936
3  6  9  3
>>> 
====================== RESTART: C:/dd/210507.py ======================
만수르 님은 돈이 많아요..
전용진 님은 돈이 많아요..
3
6
9
[3, 6, 9] 2061852557248
2061852557248 2061852557248
3  6  9  None
Traceback (most recent call last):
  File "C:/dd/210507.py", line 44, in <module>
    print(SUM(*a))
TypeError: SUM() takes 1 positional argument but 3 were given
>>> 
====================== RESTART: C:/dd/210507.py ======================
만수르 님은 돈이 많아요..
전용진 님은 돈이 많아요..
3
6
9
[3, 6, 9] 2141717872576
2141717872576 2141717872576
3  6  9  None
None
>>> 
====================== RESTART: C:/dd/210507.py ======================
만수르 님은 돈이 많아요..
전용진 님은 돈이 많아요..
None
None
None
>>> 
====================== RESTART: C:/dd/210507.py ======================
None
None
None
>>> 
====================== RESTART: C:/dd/210507.py ======================
18
21
18
>>> 
=============== RESTART: C:/dd/210507 python_3 지역변수.py ===============
black 검정
yellow 노랑
blue 파랑
>>> 
=============== RESTART: C:/dd/210507 python_3 지역변수.py ===============
black 검정
yellow 노랑
blue 파랑
Traceback (most recent call last):
  File "C:/dd/210507 python_3 지역변수.py", line 59, in <module>
    disp_color(**color)
  File "C:/dd/210507 python_3 지역변수.py", line 57, in disp_color
    pprint(x['black'], x['yellow'], x[blue])
NameError: name 'pprint' is not defined
>>> 
=============== RESTART: C:/dd/210507 python_3 지역변수.py ===============
black 검정
yellow 노랑
blue 파랑
Traceback (most recent call last):
  File "C:/dd/210507 python_3 지역변수.py", line 59, in <module>
    disp_color(**color)
  File "C:/dd/210507 python_3 지역변수.py", line 57, in disp_color
    pprint(x['black'], x['yellow'], x['blue'])
NameError: name 'pprint' is not defined
>>> 
=============== RESTART: C:/dd/210507 python_3 지역변수.py ===============
black 검정
yellow 노랑
blue 파랑
Traceback (most recent call last):
  File "C:/dd/210507 python_3 지역변수.py", line 59, in <module>
    disp_color(**color)
  File "C:/dd/210507 python_3 지역변수.py", line 57, in disp_color
    pprint(x['black'], x['yellow'], x['blue'])
NameError: name 'pprint' is not defined
>>> 
=============== RESTART: C:/dd/210507 python_3 지역변수.py ===============
black 검정
yellow 노랑
blue 파랑
검정 노랑 파랑
black 검정
yellow 노랑
blue 파랑
검정 노랑 파랑
>>> 
=============== RESTART: C:/dd/210507 python_3 지역변수.py ===============
black 검정
yellow 노랑
blue 파랑
검정 노랑 파랑
>>> 
=============== RESTART: C:/dd/210507 python_3 지역변수.py ===============
2  x ==>  100
  gg ==>   2
2 30000
  gg ==>   2
>>> def plus(x, y):
	return x+y

>>> plus(10,30)
40
>>> id(plus)
1718351399808
>>> k = 50
>>> k2 = 50
>>> id(k), id(k2)
(1718311087952, 1718311087952)
>>> p = plus
>>> id(plus), id(p)
(1718351399808, 1718351399808)
>>> plus(2, 3)
5
>>> p(3, 5)
8
>>> for i in range(1, 11):
	p(i, i+1)

	
3
5
7
9
11
13
15
17
19
21
>>> a2 = list(filter(f, range(1, 11)))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a2 = list(filter(f, range(1, 11)))
NameError: name 'f' is not defined
>>> a2 = list(filter(p, range(1, 11)))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a2 = list(filter(p, range(1, 11)))
TypeError: plus() missing 1 required positional argument: 'y'
>>> a2 = list(filter(lambda x:x*x, range(1, 11)))
>>> 2
2
>>> a2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a2 = list(map(lambda x:x*x, range(1, 11)))
>>> a2
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> filter()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    filter()
TypeError: filter expected 2 arguments, got 0
>>> help(filter)
Help on class filter in module builtins:

class filter(object)
 |  filter(function or None, iterable) --> filter object
 |  
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> list(map(lambda x:x*x, range(1, 11)))
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
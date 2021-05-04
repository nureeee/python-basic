Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(__buitins__)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dir(__buitins__)
NameError: name '__buitins__' is not defined
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> a=input()
a=100
>>> a=input()
100
SyntaxError: multiple statements found while compiling a single statement
>>> a = input()
100
>>> a
'100'
>>> type(a)
<class 'str'>
>>> a+100
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a+100
TypeError: can only concatenate str (not "int") to str
>>> int(a)
100
>>> int(a)+100
200
>>> a=int(input())
400
>>> a
400
>>> a=int(input('정수입력:'))
정수입력:500
>>> city=input('어ㅣ서 오셨낭:')
어ㅣ서 오셨낭: 부산사
>>> city
' 부산사'
>>> a= float(input('실수 입력: '))
실수 입력: 20.545
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
20.545
>>> print(a,city)
20.545  부산사
>>> pri
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    pri
NameError: name 'pri' is not defined
>>> print('aa\t bb\t cc\n dd\t ee\a ff\b gg')
aa	 bb	 cc
 dd	 ee ff gg
>>> 	print("서울은 좁아요""아주 좁아요"'정말 좁아요')
	
SyntaxError: unexpected indent
>>> print("서울은 좁아요""아주 좁아요"'정말 좁아요')
서울은 좁아요아주 좁아요정말 좁아요
>>> print("서울은 좁아요\t\t""아주 좁아요\n"'정말 좁아요')
서울은 좁아요		아주 좁아요
정말 좁아요
>>> age=20
>>> name='빌 게이츠'
>>> print(nanme, :'님은', age, '살')
SyntaxError: invalid syntax
>>> print(nanme, '님은', age, '살')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(nanme, '님은', age, '살')
NameError: name 'nanme' is not defined
>>> print(name, '님은', age, '살')
빌 게이츠 님은 20 살
>>> print('%s, %d' %(name,age))
빌 게이츠, 20
>>> print('[%d] [%10d] [%-10d] ' %(5,5,5))
[5] [         5] [5         ] 
>>> print{'{} {}',format(10,'seoul'))
SyntaxError: invalid syntax
>>> print('{} {}',format(10,'seoul'))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print('{} {}',format(10,'seoul'))
ValueError: Invalid format specifier
>>> print('{} {}', format(10,'seoul'))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print('{} {}', format(10,'seoul'))
ValueError: Invalid format specifier
>>> print('{} {}', .format(10,'seoul'))
SyntaxError: invalid syntax
>>> 
>>> print('{} {}' .format(10,'seoul'))
10 seoul
>>> print('{} {} {}' .format(10, 30,'seoul'))
10 30 seoul
>>> print('{0} {0} {1}' .format(10, 30,'seoul'))
10 10 30
>>> print('[{:20}] [{:20}] [{:10}]' .format(10, 30,'seoul'))
[                  10] [                  30] [seoul     ]
>>> print('[{:<20}] [{:<20}] [{:<10}]' .format(10, 30,'seoul'))
[10                  ] [30                  ] [seoul     ]
>>> print('[{:>20}] [{:>20}] [{:>10}]' .format(10, 30,'seoul'))
[                  10] [                  30] [     seoul]
>>> print('[{:>20}] [{:>20}] [{:^10}]' .format(10, 30,'seoul'))
[                  10] [                  30] [  seoul   ]
>>> print('[{:>20}] [{:^20}] [{:^10}]' .format(10, 30,'seoul'))
[                  10] [         30         ] [  seoul   ]
>>> print('[{:>20}] [{:^20}] [{:^10}]' .format(10, 3.14,'seoul'))
[                  10] [        3.14        ] [  seoul   ]
>>> print('[{:>20}] [{:%f}] [{:^10}]' .format(10, 3.14,'seoul'))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print('[{:>20}] [{:%f}] [{:^10}]' .format(10, 3.14,'seoul'))
ValueError: Invalid format specifier
>>> print('[{:>20}] [{:2f}] [{:^10}]' .format(10, 3.14,'seoul'))
[                  10] [3.140000] [  seoul   ]
>>> print('[{:>20}] [{:.10f}] [{:^10}]' .format(10, 3.14,'seoul'))
[                  10] [3.1400000000] [  seoul   ]
>>> 
>>> 
>>> print('%f,  %.2f, %.10f' .format(2.13, 2.13, 2.13))
%f,  %.2f, %.10f
>>> print('%f,  %.2f, %.10f' % (2.13, 2.13, 2.13))
2.130000,  2.13, 2.1300000000
>>> print('{:%f},  %.2f, %.10f' % (2.13, 2.13, 2.13))
{:2.130000},  2.13, 2.1300000000
>>> print('{:%2f},  %.2f, %.10f' % (2.13, 2.13, 2.13))
{:2.130000},  2.13, 2.1300000000
>>> print('{:2f},  %.2f, %.10f' % (2.13, 2.13, 2.13))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print('{:2f},  %.2f, %.10f' % (2.13, 2.13, 2.13))
TypeError: not all arguments converted during string formatting
>>> print('{:f},  %.2f, %.10f' .format(2.13, 2.13, 2.13))
2.130000,  %.2f, %.10f
>>> 
>>> 
>>> sum=0
>>> range(10)
range(0, 10)
>>> range(1,11)
range(1, 11)
>>> for i in range(10)
SyntaxError: invalid syntax
>>> for i in range(10):
	print(i)

0
1
2
3
4
5
6
7
8
9
>>> for i range(5,101,5):
	
SyntaxError: invalid syntax
>>> for i in range(5,101,5):
	print(i, end=\t)
	
SyntaxError: unexpected character after line continuation character
>>> for i in range(5,101,5):
	print(i, end='\t')

5	10	15	20	25	30	35	40	45	50	55	60	65	70	75	80	85	90	95	100	
>>> for i in range(5,101,5):
	print(i, end='  ')

	
5  10  15  20  25  30  35  40  45  50  55  60  65  70  75  80  85  90  95  100  
>>> for i in range(,10,2):
	print(i, end='\n')
	
SyntaxError: invalid syntax
>>> for i in range(010,2):
	print(i, end='\n')
	
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> for i in range(10,2):
	print(i, end='\n')

	
>>> 
>>> for i in range(10,2):
	print(i, end='\n')

	
>>> 
>>> 
>>> 
>>> Sum = 0
>>> for i in range(1, 11):
	Sum=Sum+i

	
>>> Sum
55
>>> for i in range(1, 101):
	Sum=Sum+i

	
>>> 
>>> print(Sum)
5105
>>> Sum=0
>>> for i in range(1, 101,2):
	Sum=Sum+i

	
>>> 
>>> print(Sum)
2500
>>> for i in range(2, 101,2):
	Sum=Sum+i

	
>>> 
>>> print()Sum
SyntaxError: invalid syntax
>>> print(Sum)
5050
>>> Sum2=0.0
>>> for i in range(100):
	Sum=Sum+0.1

	
>>> for i in range(100):
	Sum2=Sum2+0.1

	
>>> 
>>> Sum2
9.99999999999998
>>> print('[%F]' %(sUM2))
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print('[%F]' %(sUM2))
NameError: name 'sUM2' is not defined
>>> print('[%f]' %(sUM2))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    print('[%f]' %(sUM2))
NameError: name 'sUM2' is not defined
>>> print('[%f]' %(Sum2))
[10.000000]
>>> print('[%.3f]' %(Sum2))
[10.000]
>>> 
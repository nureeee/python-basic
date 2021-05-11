Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(__biltins__)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dir(__biltins__)
NameError: name '__biltins__' is not defined
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> b = [4, 7, 2]
>>> sorted(b)
[2, 4, 7]
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> sorted(b) ##함수
[2, 4, 7]
>>> b.sort()  ##멤버함수
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(object) #최상위
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> 
>>> a = [i for i in range(1, 101, 2)]
>>> a
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> next(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    next(a)
TypeError: 'list' object is not an iterator
>>> type(a)
<class 'list'>
>>> import sys
>>> k = 10
>>> k1 = 20
>>> k2 = 'koreakorea'
>>> sys.getsizeof(k)
28
>>> sys.getsizeof(k1)
28
>>> sys.getsizeof(k2)
59
>>> t1 = [2, 3, 5]
>>> sys.getsizeof(t1)
120
>>> a = [i for i in range(1, 101, 2)]
>>> len(a)
50
>>> sys.getsizeof(a)
472
>>> a = [i for i in range(1, 101)]
>>> sys.getsizeof(a)
920
>>> a = [i for i in range(1, 1001)]
>>> sys.getsizeof(a)
8856
>>> a = [i for i in range(1, 1001)]
>>> b = [i for i in range(1, 101, 2)]
>>> sys.getsizeof(b)
472
>>> b = (i for i in range(1, 101, 2))
>>> b = (i for i in range(1, 101))
>>> b = (i for i in range(1, 101, 2))
>>> sys.getsizeof(b)
112
>>> b = (i for i in range(1, 101))
>>> sys.getsizeof(b)
112
>>> b = (i for i in range(1, 1001))
>>> sys.getsizeof(b)
112
>>> -
SyntaxError: invalid syntax
>>>  = [i for i in range(1, 101, 2)]
 
SyntaxError: unexpected indent
>>> a = [i for i in range(1, 101, 2)]
>>> a2 = iter(a)
>>> sys.getsizeof(a)
472
>>> sys.getsizeof(a2)
48
>>> len(a2)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    len(a2)
TypeError: object of type 'list_iterator' has no len()
>>> len(a)
50
>>> next(a2)
1
>>> type(a2)
<class 'list_iterator'>
>>> 
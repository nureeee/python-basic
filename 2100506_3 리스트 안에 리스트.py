Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [3, 4, 5, [3, 4, 5]]
>>> a
[3, 4, 5, [3, 4, 5]]
>>> b = a.pop()
>>> b
[3, 4, 5]
>>> b[2] =43
>>> b
[3, 4, 43]
>>> a.append(b)
>>> a
[3, 4, 5, [3, 4, 43]]
>>> b
[3, 4, 43]
>>> b.remove(43)
>>> b
[3, 4]
>>> a.pop()
[3, 4]
>>> a
[3, 4, 5]
>>> b
[3, 4]
>>> a.append(b)
>>> a
[3, 4, 5, [3, 4]]
>>> b
[3, 4]
>>> 
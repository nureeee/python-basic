print('*'* 30)
print('hello')

a = [3, 5, 6]

print("king" + "ace")

print("king" * 3)

print(a * 3)


try:
    a + 2
except (TypeError, IndexError):
    print('미안미안')

try:
    a[2] / 0
except ZeroDivisionError as msg:  ##에러메세지를 불러온다.?
    print(msg,'입니다.')
    

print('bye~~')
print('*'* 30)






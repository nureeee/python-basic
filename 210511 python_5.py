print('start')
try:
    2 / 0
except ZeroDivisionError as msg :
    print(msg)

a = [1, 2, 3]

try:
    # a[3] = 4
    #"kora" + 4
    4 / 0

# except IndexError as msg :
#     print(msg)

# except TypeError as msg:
#     print(msg)

# except ZeroDivisionError as msg:
#     print(msg)

except(IndexError, TypeError, ZeroDivisionError):
    print(' 셋 중 하나....')


else :
    print('IndexError, TypeError, ZeroDivisionError 아니다. ')


finally:
    print('에러와 상관없이 무조건 실행.. ')

print('** end *** ')
[출처] AII - 6일차 (양주종의 코딩스쿨 ▶ C언어 ·파이썬 ·리눅스 ·정보처리기사) | 작성자 양주종

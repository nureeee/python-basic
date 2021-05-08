'''
dan = int(input(" 몇 단 출력할까요 : "))
for i in range(1, 10):
    print("{} * {} = {}".format(dan, i, dan*i))

'''
'''

while True:

    dan = int(input(" 몇 단 출력할까요 : "))
    if dan == 0:
        print(" 프로그램 종료 ")
        break

    if dan < 2 or dan > 9:
        print("범위를 벗어났어요.")
        continue

    for i in range(1, 10):
        print("{} * {} = {}".format(dan, i, dan*i))

'''
'''

sum = 0

for i in range(1, 101):
    sum = sum + i
    print(" i => {:2d}, sum => {:3d}" .format(i, sum))

print(" sum = {}" .formata(sum))
'''

'''

sum = 0

for i in range(100, 0, -2):
    sum = sum + i
    print(" i => {:2d}, sum => {:3d}" .format(i, sum))

print(" sum = {}" .formata(sum))

'''
'''

name = None

for i in range(5):
    name = input(" 이름은 : ")
    print("반갑습니다. {}님". format(name))

'''
'''
i = 0
while i < 11:
    print(" i ==> {}".format(i))
    i = i+1
'''
'''

i = 1
sum = 0

while i <=10:
    print("i ==> {}" .format(i))
    sum = sum +i
    i = i + 1
print("sum = {}".format(sum))

'''

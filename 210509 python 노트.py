'''
i = 1
Sum = 0

while i <= 10:
    print (" i ==> {}".format(i))
    Sum = Sum + i
    i = i+1
print("Sum = {} * {} = {}".format(Sum))
'''
'''
dan = int(input("출력할 단은 :"))
i = 1

while i < 10:
    print("{} * {} = {} ".format(dan, i, dan*i))
    i = i+1
    
print("-------------------")
for j in range(1, 10):
    print("{} * {} = {}".format(dan, j, dan*j))

'''
'''
i = 0
while i < 3:
    print(" i ==> {}".format(i))

    j = 0
    while j in range(5):
        print(" i ==> {}, j ==> {}".format(i, j))
        j = i + 1

        i = i + 1
'''
'''

i = 2
while i < 10:
    print(" {}단 ".format(i))

    j = 1
    while j < 10:
        print(" {} * {} = {}".format(i, j, i*j))
        j = j + 1

    i = i+1
'''
'''

for i in range(2, 10):
    print(" = {}단 = ".format(i))

    for j in range(1, 10):
        print(" {} * {} = {}".format(i, j, i*j))
'''
'''
import sys

while True:
    city = input(" 인구가 가장 많은 도시는 :")

    while city == "서울":
        print(" {} 딩동댕 ~~".format(city))
        print(" 프로그램 종료")
        sys.exit() 
    
'''
'''

import sys

while True:
    num = int(input(" 행운의 숫자는 : "))

    while num == 777:
        print(" {} 딩동댕~~".format(num))
        print( " 프로그램 종료 ")
        sys.exit()
        
'''
'''

if 2 > 3:
    
    print(" 참 ")
    print(" 참 맛있다. ")
else:
    print(" 거짓 ")
    print(" 그 집 별로야~~")

print(" 오늘은 좋은 날 ")

'''

'''
while True:
    
    score = int(input(" 점수입력 : "))

    if score == 0:
        break

    if score >= 90:
        print( score, "점 ===> 수 ")

    elif score >= 80:
        print(score, "점 ===> 우 ")

    elif score >= 70:
        print(score, "점 ===> 미 ")

    elif score >= 60:
        print(score, "점 ===> 양 ")

    else: 
        print(score, "점 ===> 노력하세요.. ")

'''
'''

while True:

    nation = input("국가 입력 : ")

    if nation == "끝":
        break

    if nation == " 대한민국 ":
        print(nation, " 참 좋은 나라입니다")

    elif nation == " 미국 ":
        print(nation, "도 좋아요.")

    elif nation == " 프랑스 ":
        print(nation, "에 살고 싶어요.")

    else:
        print(nation, "생각 해 볼께요.")

'''
'''

for i in range(1, 11):
    if i == 3:
        continue
    print(" i ==> {}".format(i))


for i in range(1, 11):
    if i == 3:
        break
    print(" i ==> {}".format(i))

'''
'''

#잘 모르겠음...

for i  in range(1, 6):
    print(" i ==> {}".format(i))

    for j in range(1, 6):
        print(" j ==> {}".format(j))

print()

'''

'''
for i in range(1, 6):
    print(" i ==> {}".format(i))

    for j in range(1, 6):
        print(" j ==> {}".format(j))
        if j == 3:
            break
'''

'''
a = []

with open("c:\\dd\\ss.txt", "r", encoding = 'utf8') as f:
    for i in range(10):
        a.append(f.readline().split())

for i in range(len(a)):
    a[i][1] = int(a[i][1])
    a[i][2] = int(a[i][2])
    a[i][3] = int(a[i][3])
    a[i].append(a[i][1] + a[i][2] + a[i][3])  
    a[i].append(a[i][4] / 3)                  

kt = et =mt = 0
for i in range(len(a)):
    kt = kt + a[i][1]
    et = et + a[i][2]
    mt = mt + a[i][3]

print("  ** 성 적 표 **  ")
print("=" * 30)
print(" 이 름 국어 영어 수학 총점 평균")
print("=" * 30)

for i in range(len(a)):
    print(" {}  {}  {}  {}  {}  {:.1f} ".format(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5]))

    print("=" * 30)

    print("평균 : {:.1f} {:.1f} {:.1f} {:.1f}".format(kt/10, et/10, mt/10, (kt+et+mt)/3/10 ))
 
'''
















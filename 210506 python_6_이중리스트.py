#for 문
'''
Sum = 0
for i in range(1, 10, 1):
    Sum = Sum +i
    print('i===>', i,"Sum==>", Sum)
'''
#2
'''
Sum = 0
for i in range(1, 101, 1):
for i in range(2, 101, 2):
for i in range(1, 101, 2):

for i in range(1, 10, -5):
    Sum = Sum +i
    print('i===>', i,"Sum==>", Sum)
'''

'''
for i in range(1,7):
    if i == 3:
        #continue(스킵하고 다시 if문 위로)
        #break 루프탈출 뒷의 내용 삭제
    print(i, end = '  ')
'''
'''
while True:
    dan = int(input(' 몇 단 출력:'))
    
    if dan == 0:
        print('good bye!!!!')
        break
    
    if dan < 2 or dan > 9:
        continue
    
    for i in range(1,10):
        print('{}*{} = {}'.format(dan, i, dan*i))
'''
#기본 if문
'''
if True:
    print('  참  ')

print('목요일')
'''
'''
if (3 < 2) and (3==3):
    print('  참  ');  print('목요일')
'''

#다중 if문
'''
while True:
    score = int(input('점수 입력 : '))
    if score == 0:
        break
    if score >100 or score < 0:
        continue
    
    if score >= 90:
        print( score, '참 잘했어요.')
        
    if score >= 90:
        print(score, '수')
    elif score >= 80:
        print(score, '우')
    elif score >= 70:
        print(score, '미')
    elif score >= 60:
        print(score, '양') 
    else:
        print(score, '가')
'''


#이중 리스트_
##성적처리
st = []
with open('c:\\dd\\ss.txt', 'r', encoding = 'utf8') as f:
    for i in range(10):
        st.append(f.readline().split())  #한 줄씩 읽기
        st[i][1] = int(st[i][1])
        st[i][2] = int(st[i][2])
        st[i][3] = int(st[i][3])
        
        ##총점, 평균
        total = st[i][1] + st[i][2] + st[i][3]
        avg = total / 3
        st[i].append(total)
        st[i].append(avg)

##과목별 평균, 반 전체 평균
total_kor = total_eng = total_mat = 0

for i in range(10):
    total_kor = total_kor + st[i][1]
    total_eng = total_eng + st[i][2]
    total_mat = total_mat + st[i][3]

avg_kor = total_kor / len(st)
avg_eng = total_eng / len(st)
avg_mat = total_mat / len(st)

'''

for i in range(10):
    print(st[i])
        
print('국어평균 : {} 영어평균 : {} 수학평균 : {}'.format(avg_kor, avg_eng, avg_mat, (avg_kor + avg_eng + avg_mat)/3))

'''
print('********** 성적표 ********')








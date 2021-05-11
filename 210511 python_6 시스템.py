import os

while True:
    print('1. 메모장')
    print('2. 계산기')
    print('3. 그림판')
    print('4. 크롬')
    print('0. 종료')

    sw = input(' 선택해 주세요. [   ]\b\b\b')

    if sw == '0':
        print(' 안녕헤 계세요. ')
        break   

    if sw == '1':
        os.system('notepad')
    elif sw == '2':
        os.system('calc')
    elif sw == '3':
        os.system('mspaint')
    elif sw == '4': 
        os.system('start chrome')    
    else:
        print(sw, ' 없는 메뉴'
[출처] AII - 6일차 (양주종의 코딩스쿨 ▶ C언어 ·파이썬 ·리눅스 ·정보처리기사) | 작성자 양주종

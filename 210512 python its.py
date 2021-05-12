import openpyxl as xl

exf = xl.load_workbook('c:\\dd\\itsal.xlsx')

aws = exf.active

tot = 0
for i in aws.rows:
    index = i[0].row
    name = i[0].value
    salary = i[1].value

    tot += salary
    avg = tot / 5

    aws.cell(row = 6, column = 2).value = avg

    print('{}  {}  '.format(name, salary))
print('"평균 연봉"  {}'.format(avg))

exf.save('c:\\dd\\outitsal.xlsx')
exf.close() 
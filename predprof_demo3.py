def readFile(filename):
    ''' Чтение csv файла в список
    param имя файла для чтения
    return list of students
    '''
    f = open(filename, 'r', encoding = 'utf-8')
    global z1,z2,z3,z4,z5
    z1,z2,z3,z4,z5=f.readline().strip().split(',')
    tab=[]
    for i in range(500):
        d1,d2,d3,d4,d5=f.readline().strip().split(',')
        tab.append([d1,d2,d3,d4,d5]) 
    return tab

tab=readFile('students.csv')
idproj=input()
while idproj!="СТОП":
    for i in range(len(tab)):
        fio=tab[i][1].split()
        if tab[i][4]==idproj:
            
            print(f'Проект №{tab[i][4]} делал: {fio[1][0]}.{fio[0]} он(а) получил(а) оценку - {tab[i][6]}.')
            break
    else:
        print('Ничего не найдено')
    idproj=input()

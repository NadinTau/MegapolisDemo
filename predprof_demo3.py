def readFile(filename):
    ''' Чтение csv файла в список
    param имя файла для чтения
    return list of students
    '''
    f = open(filename, 'r', encoding = 'utf-8')
    tab=[]
    for i in range(501):
        d0,d1,d2,d3,d4=f.readline().strip().split(',')
        tab.append([d0,d1,d2,d3,d4]) 
    return tab


tab=readFile('students.csv')
idproj=input()
while idproj!="СТОП":
    for i in range(1,len(tab)):
        fio=tab[i][1].split()
        if tab[i][2]==idproj:
            
            print(f'Проект №{tab[i][2]} делал: {fio[1][0]}.{fio[0]} он(а) получил(а) оценку - {tab[i][4]}.')
            break
    else:
        print('Ничего не найдено')
    idproj=input()

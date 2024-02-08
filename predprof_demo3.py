f=open('students.csv')
z1,z2,z3,z4,z5=f.readline().split(',') #считываем строку с заголовками
tab=[] #это будет двухмерный список со всеми данными
fio=[] #ФИО через пробел, а удобно работать по отдельности

#создаем двухмерный список данных из файла:
for i in range(500):
    d1,d2,d3,d4,d5=f.readline().strip().split(',') #прочитали строку из файла, разбили
    fio=d2.split() # разбили ФИО на фамилию, имя, отчество отдельно
    # создаем двухмерный список с исходными данными
    tab.append([d1,fio[0],fio[1],fio[2],d3,d4,d5]) 


idproj=input()
while idproj!="СТОП":
    for i in range(len(tab)):
        if tab[i][4]==idproj:
            print(f'Проект №{tab[i][4]} делал: {tab[i][2][0]}.{tab[i][1]} он(а) получил(а) оценку - {tab[i][6]}.')
            break
    else:
        print('Ничего не найдено')
    idproj=input()

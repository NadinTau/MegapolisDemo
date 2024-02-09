def readfile(namefile):
    '''
    Read file and create list of students
    :param namefile: str, name file
    :return: list of students
    '''
    f=open(namefile,'r',encoding='utf-8')
    students=[]
    for i in range(501):
        students.append(f.readline().strip().split(','))
    return students

def findstudent(idpr):
    '''
    Поиск данных по учащемуся и вывод на экран
    :param family: фамилия, str
    :param name: имя, str
    :return: -
    '''
    for i in range(1,501):
        if students[i][2] == idpr:
            f,im,o=students[i][1].split()
            print(f'Проект № {idpr} делал: {im[0]}.{f} он(а) получил(а) оценку - {students[i][4]}.')
            break
    else: print('Ничего не найдено.')

students=readfile('/home/teacher/Загрузки/students.csv')
idpr=input()
while idpr!='СТОП':
    findstudent(idpr)
    idpr = input()
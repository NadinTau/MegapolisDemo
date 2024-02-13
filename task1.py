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
        if students[i][4]=='None':
            students[i][4]='0'
    return students

def aver(clas):
    '''
    Нахождение среднего арифметического оценок учащихся класса
    :param clas: str, class number
    :return: float, average mark
    '''
    summ=0
    n=0
    for i in range (1,501):
        if students[i][3]==clas and students[i][4]!='0':
            summ+=int(students[i][4])
            n+=1
    return format(summ/n,'.3f')

def repl():
    '''Замена ошибочной оценки 'None' на среднюю орифметическую по классу
    '''
    for i in range(1,501):
        if students[i][4]=='0':
            students[i][4] = str(aver(students[i][3]))

def writefile(name):
    '''
    Write new file with hash-key
    :param name: str, name file
    '''
    f = open(name, 'w', encoding='utf-8')
    f.write(','.join(students[0])+'\n')
    for i in range(1,501):
        f.write(','.join(students[i]) + '\n')
    f.close()


students=readfile('/home/teacher/Загрузки/students.csv')
repl()
writefile('/home/teacher/Загрузки/student_new.csv')
